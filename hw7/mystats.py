import numpy as np
import scipy as sp
import scipy.stats as stats

def t_interval(data, conf=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = a.mean(), stats.sem(a)
    h = se * stats.t.ppf((1+conf)/2., n-1)
    return m-h, m+h