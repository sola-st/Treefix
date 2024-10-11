self = type('Mock', (object,), {'assertDatasetProduces': lambda x, y: None})() # pragma: no cover

from types import SimpleNamespace # pragma: no cover

self = type('Mock', (object,), {'assertDatasetProduces': lambda x, y, z: print('Assertion passed with:', y, z)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
