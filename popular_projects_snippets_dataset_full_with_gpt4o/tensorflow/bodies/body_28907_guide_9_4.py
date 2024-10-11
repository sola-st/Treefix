class Mock: pass # pragma: no cover
def assertDatasetProduces(self, ds, expected_output): # pragma: no cover
    actual_output = [(x, y) for x, y in ds.as_numpy_iterator()] # pragma: no cover
    assert actual_output == expected_output, f'Expected {expected_output}, but got {actual_output}' # pragma: no cover
self = type('Mock', (object,), {'assertDatasetProduces': assertDatasetProduces})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
