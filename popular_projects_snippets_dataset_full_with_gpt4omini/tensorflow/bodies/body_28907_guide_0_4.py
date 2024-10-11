class MockTest: pass # pragma: no cover
self = MockTest() # pragma: no cover
def assertDatasetProduces(ds, expected): pass # pragma: no cover
self.assertDatasetProduces = assertDatasetProduces # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
