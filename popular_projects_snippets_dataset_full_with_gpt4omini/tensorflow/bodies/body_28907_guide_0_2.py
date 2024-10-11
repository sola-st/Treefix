import unittest # pragma: no cover

class TestDataset(unittest.TestCase): # pragma: no cover
    def assertDatasetProduces(self, ds, expected): # pragma: no cover
        actual = list(ds.as_numpy_iterator()) # pragma: no cover
        self.assertEqual(actual, expected) # pragma: no cover
test_case = TestDataset() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
