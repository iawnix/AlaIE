import numpy as np
import pandas as pd
from numpy.typing import NDArray
from rich.progress import track
from rich import print as rp

def cal_InterEntropy_aa(wi_aa: NDArray, BETA: float):
    E_int = np.sum(2*wi_aa[:, [2, 3]], axis = 1)        # vdw_vac + ele_vac
    E_int_mean = np.mean(E_int)
    return np.log(np.mean(np.exp(BETA*(E_int - E_int_mean))))


