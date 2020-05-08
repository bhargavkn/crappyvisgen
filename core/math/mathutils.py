import numpy as np
from statistics import stdev, mean


def percentile(array, q):
    a = np.array(array)
    return np.percentile(a, q)