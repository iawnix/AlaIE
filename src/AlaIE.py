import numpy as np
import pandas as pd
from numpy.typing import NDArray
from rich.progress import track
from rich import print as rp

class alascan_dec_ene():
    def __init__(self, fp: str) ->  None:
        self.fp = fp
        self.key = "DELTA,Total Energy Decomposition:\n"
        self.raw_col = ["Frame","Residue","Location","Int","vdW","ele","GB","nonpol","tol"]
        self.ene_col = ["Int", "vdW", "ele", "GB", "nonpol", "tol"]

    def convert_to_matrix(self, df, resid):

        split_resid = lambda _: int(_.split(" ")[-1])

        df.columns = self.raw_col
        df["resid"] = df["Residue"].apply(split_resid)
        df = df.drop(columns=["Residue", "Location"]).copy()

        df = df[df["resid"] == resid][["Frame"]+self.ene_col]
        df = df.reset_index(drop=True)
        df["Frame"] = df["Frame"].astype("int")
        for col in self.ene_col:
            df[col] = df[col].astype("float64")

        return df.to_numpy()

    def __call__(self, resid: int):
        
        with open(self.fp, "r") as F:
            ss = F.readlines()

        # Frame #,Residue,Location,Internal,van der Waals,Electrostatic,Polar Solvation,Non-Polar Solv.,TOTAL
        # +2 矫正到纯数据行
        key_start_s = []
        key_end_s = []
        flag = False
        for i, s in enumerate(ss):
            if s == self.key:
                key_start_s.append(i+2)
                flag = True
            if flag and s == "\n":
                key_end_s.append(i)
                flag = False
        assert len(key_start_s) == 2 and len(key_end_s) == 2, print("Error[iaw]>: must the dec ene for ala scan")

        df_wi = pd.DataFrame(np.genfromtxt(ss[key_start_s[0]:key_end_s[0]+1],delimiter=',',dtype=str))
        wi = self.convert_to_matrix(df_wi, resid)

        df_mut = pd.DataFrame(np.genfromtxt(ss[key_start_s[1]:key_end_s[1]+1],delimiter=',',dtype=str))
        mut = self.convert_to_matrix(df_mut, resid)

        return wi, mut


def cal_InterEntropy_aa(wi_aa: NDArray, BETA: float):
    E_int = np.sum(2*wi_aa[:, [2, 3]], axis = 1)        # vdw_vac + ele_vac
    E_int_mean = np.mean(E_int)
    return np.log(np.mean(np.exp(BETA*(E_int - E_int_mean))))


K = 1.9872E-3  # kcal/(mol·K)
T = 300        # k
BETA = 1/(K*T) # mol/kcal
out = {}
for fp in track(["12_SER","14_ASN","15_SER","16_ARG","185_PRO","186_HIE","188_PHE","189_PHE","191_PHE","192_PRO","193_VAL","194_THR"
        ,"197_ILE","199_PRO","201_TYR","20_GLN","21_VAL","236_MET","239_ASN","23_PHE","243_TYR","244_ASN","248_THR","249_VAL"
        ,"250_TYR","253_LEU","33_PRO","35_TRP","37_ASN","38_PHE","43_GLN","45_TYR","46_PRO","47_THR","48_LEU","54_ARG"
        ,"55_ARG","56_ILE","57_HIE","58_SER","59_TYR","62_HID","64_TRP","66_PHE"]):
    resid, resn = fp.split("_")
    resid = int(resid)
    m_wi, m_mut = alascan_dec_ene(fp = "/home/iaw/DATA/IE/test/data/{}.csv".format(fp))(resid)
    ie = K*T*(cal_InterEntropy_aa(m_mut, BETA) - cal_InterEntropy_aa(m_wi, BETA))
    
    out[str(resid)] = ie

ie_all = np.sum(np.array(list(out.values())))
rp(out)
rp(ie_all)