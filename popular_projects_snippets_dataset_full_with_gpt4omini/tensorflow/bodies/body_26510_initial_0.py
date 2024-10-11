import numpy as np # pragma: no cover

class _AssertCardinalityDataset:# pragma: no cover
    def __init__(self, dataset, expected_cardinality):# pragma: no cover
        self.dataset = dataset# pragma: no cover
        self.expected_cardinality = expected_cardinality# pragma: no cover
    def __call__(self):# pragma: no cover
        return len(self.dataset) == self.expected_cardinality # pragma: no cover
dataset = np.array([1, 2, 3, 4, 5]) # pragma: no cover
expected_cardinality = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/cardinality.py
from l3.Runtime import _l_
aux = _AssertCardinalityDataset(dataset, expected_cardinality)
_l_(8731)
exit(aux)
