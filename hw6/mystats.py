from scipy.stats import beta
 
def binom_interval(success, total, conf=0.95):
    quantile = (1 - conf) / 2.
    lower = beta.ppf(quantile, success, total - success + 1)
    upper = beta.ppf(1 - quantile, success + 1, total - success)
    return (lower, upper)