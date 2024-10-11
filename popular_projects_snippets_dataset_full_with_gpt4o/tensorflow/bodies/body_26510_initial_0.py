_AssertCardinalityDataset = lambda dataset, expected_cardinality: dataset == expected_cardinality # pragma: no cover
dataset = 'sample_data' # pragma: no cover
expected_cardinality = 'sample_data' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/cardinality.py
from l3.Runtime import _l_
aux = _AssertCardinalityDataset(dataset, expected_cardinality)
_l_(21142)
exit(aux)
