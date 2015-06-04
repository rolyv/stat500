import pandas as pd
import numpy as np
from types import *

def quartile(a, quartile=1):
    assert (type(quartile) is IntType) & (quartile in range(1,4)), "Quartile must be an integer in range [1,3]"
    
    a = a[~ pd.isnull(a)]
    a = a.sort(inplace=False)
    
    pos1 = (len(a) + 1) * quartile / 4.0
    round_pos1 = int(np.floor(pos1))
    first_part = a.iloc[round_pos1 - 1]
    extra_prop = pos1 - round_pos1
    interp_part = extra_prop * (a.iloc[round_pos1] - first_part)
    
    return first_part + interp_part