import sys
sys.path.insert(0, ".")
import unittest
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from WeightedCorr import WeightedCorr


class TestUnweighted(unittest.TestCase):
    def test_unweighted(self):
        z1 = np.random.randn(1000, 2) + 2
        z2 = np.random.randn(1000, 2) - 2 
        z = np.concatenate([z1, z2], axis=0)

        scipy_result = spearmanr(z).correlation
    
        w = np.ones(len(z))    
        result = WeightedCorr(
            x=pd.Series(z[:, 0]),
            y=pd.Series(z[:, 1]),
            w=pd.Series(w)
        )(method="spearman")

        self.assertAlmostEqual(scipy_result, result)


