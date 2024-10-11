self = type('Mock', (object,), {'assertDatasetProduces': lambda self, ds, expected: print(f'Dataset produced: {list(ds.as_numpy_iterator())}, Expected output: {expected}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
