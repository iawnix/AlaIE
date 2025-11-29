from typing import Tuple, Callable
import numpy as np
import pandas as pd
from numpy.typing import NDArray
from rich.progress import track
from rich import print as rp
import argparse
import time

def timeit(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)
        end_time = time.time()
        rp("Function {} took {:.4f} s to execute.".format(func.__name__, end_time - start_time))
        return result
    return wrapper


class alascan_dec_ene():
    def __init__(self, fp: str, enable_timeit: bool = False) ->  None:
        self.fp = fp
        self.key = "DELTA,Total Energy Decomposition:\n"
        self.raw_col = ["Frame","Residue","Location","Int","vdW","ele","GB","nonpol","tol"]
        self.ene_col = ["Int", "vdW", "ele", "GB", "nonpol", "tol"]
        self.enable_timeit = enable_timeit

    def convert_to_matrix(self, df, resid) -> NDArray:
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

    def __call__(self, resid: int) -> Tuple[NDArray, NDArray]:
        if self.enable_timeit:
            return self.__run_timeit(resid)
        else:
            return self.__run(resid)

    @timeit
    def __run_timeit(self, resid: int) -> Tuple[NDArray, NDArray]:
        return self.__run(resid)

    def __run(self, resid: int) -> Tuple[NDArray, NDArray]:
        
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
        assert len(key_start_s) == 2 and len(key_end_s) == 2, rp("Error[iaw]>: must the dec ene for ala scan")

        df_wi = pd.DataFrame(np.genfromtxt(ss[key_start_s[0]:key_end_s[0]+1],delimiter=',',dtype=str))
        wi = self.convert_to_matrix(df_wi, resid)

        df_mut = pd.DataFrame(np.genfromtxt(ss[key_start_s[1]:key_end_s[1]+1],delimiter=',',dtype=str))
        mut = self.convert_to_matrix(df_mut, resid)

        return wi, mut


def Parm():

    parser = argparse.ArgumentParser(description='IAWNIX: Based on the work of John Z. H. Zhang et al.[DOI: 10.1021/acs.jctc.7b01295], this implementation was carried out.')
    parser.add_argument('-AlaDecPath'
                        , type = str
                        , nargs = 1
                        , help = '所有的丙氨酸扫描的结果文件, 命名: 12_SER.csv')
    parser.add_argument('-T'
                        , type = float
                        , nargs = 1
                        , help = '模拟温度, 默认300K'
                        , default=[300.0])
    parser.add_argument('-out'
                        , type = str
                        , nargs=1
                        , help='输出文件路径')
    parser.add_argument('-debug'
                        , type = bool
                        , nargs=1
                        , help='调试'
                        , default=[False])
    

    return parser.parse_args()
