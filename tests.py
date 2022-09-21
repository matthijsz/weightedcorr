import sys
sys.path.insert(0, ".")
import unittest
import pandas as pd
import numpy as np
from scipy.stats import spearmanr, rankdata
from WeightedCorr import WeightedCorr


def get_weighted_rank(x, w):
    x_rank = rankdata(x, method="average")

    a, b = [], []
    for i in range(len(x_rank)):
        curr_rank = x_rank[i]
        up_to_curr = x_rank < curr_rank
        sum_w = np.sum(w[up_to_curr])
        a.append(sum_w)

        tied_with_curr = x_rank == curr_rank
        n = np.sum(tied_with_curr)
        mean_w = np.mean(w[tied_with_curr])
        b.append(mean_w*(n+1)/2)

    return np.array(a) + np.array(b)


class TestUnweighted(unittest.TestCase):
    def test_unweighted(self):
        # create 2 gaussians centered at different locations
        z1 = np.random.randn(1000, 2) + 2
        z2 = np.random.randn(1000, 2) - 2 

        # concatenate
        z = np.concatenate([z1, z2], axis=0)

        scipy_result = spearmanr(z).correlation
    
        w = np.ones(len(z))    
        result = WeightedCorr(
            x=pd.Series(z[:, 0]),
            y=pd.Series(z[:, 1]),
            w=pd.Series(w)
        )(method="spearman")

        self.assertAlmostEqual(scipy_result, result)



class TestWeighted(unittest.TestCase):
    def test_weighted(self):
        z1 = np.random.randn(1000, 2) + 2
        z2 = np.random.randn(1000, 2) - 2 
        z = np.concatenate([z1, z2], axis=0)

        w = np.arange(1, len(z)+1)

        wx = get_weighted_rank(z[:, 0], w)
        wy = get_weighted_rank(z[:, 1], w)

        wx_bar = np.sum(w*wx)/np.sum(w)
        wy_bar = np.sum(w*wy)/np.sum(w)

        numerator = np.sum(w*(wx-wx_bar)*(wy-wy_bar))
        denominator = np.sqrt(np.sum(w*((wx-wx_bar)**2))*np.sum(w*((wy-wy_bar)**2)))

        correct_result = numerator/denominator

        result = WeightedCorr(
            x=pd.Series(z[:, 0]),
            y=pd.Series(z[:, 1]),
            w=pd.Series(w)
        )(method="spearman")

        self.assertAlmostEqual(correct_result, result)