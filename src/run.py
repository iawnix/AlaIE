
from typing import Dict
import numpy as np
from numpy.typing import NDArray
from rich.progress import track
from rich import print as rp
from glob import glob

import sys, os
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from .util.cal import cal_InterEntropy_aa
from .util.tools import alascan_dec_ene, Parm
from .util.constants import K, T, BETA


def get_all_dec_csv(dp: str) -> Dict:
    out = {}
    fps = glob(dp + "/" + "*.csv")
    for fp in fps:
        resid_resn_csv = os.path.basename(fp)
        resid_resn = resid_resn_csv.rstrip(".csv")
        out[resid_resn] = fp
    return out

def main() -> None:
    parm = Parm()
    dec_path = parm.AlaDecPath[0]
    T = parm.T[0]
    BETA = 1/(K*T) # mol/kcal
    outf = parm.out[0]
    fp_dcit = get_all_dec_csv(dec_path)
    debug = parm.debug[0]

    IE_AA = {}
    if debug:
        for resid_resn in list(fp_dcit.keys()):
            resid, resn = resid_resn.split("_")
            resid = int(resid)
            fp = fp_dcit[resid_resn]
            m_wi, m_mut = alascan_dec_ene(fp = fp, enable_timeit=True)(resid)
            ie = K*T*(cal_InterEntropy_aa(m_mut, BETA) - cal_InterEntropy_aa(m_wi, BETA))
            IE_AA[str(resid)] = ie
    else:
        for resid_resn in track(list(fp_dcit.keys())):
            resid, resn = resid_resn.split("_")
            resid = int(resid)
            fp = fp_dcit[resid_resn]
            m_wi, m_mut = alascan_dec_ene(fp = fp)(resid)
            ie = K*T*(cal_InterEntropy_aa(m_mut, BETA) - cal_InterEntropy_aa(m_wi, BETA))
            IE_AA[str(resid)] = ie
       

    ie_all = np.sum(np.array(list(IE_AA.values())))
    rp("#++++++++++++++++++++++++++++++++++++++++++#")
    rp(IE_AA)
    rp("#++++++++++++++++++++++++++++++++++++++++++#")
    rp("InterEntropy: {:.6f}".format(ie_all))
    with open(outf, "w+") as F:
        for k,v in IE_AA.items():
            F.writelines("{}, {:.6f}\n".format(k, v))
        F.writelines("tol, {:.6f}\n".format(ie_all))

if __name__ == "__main__":
    main()
