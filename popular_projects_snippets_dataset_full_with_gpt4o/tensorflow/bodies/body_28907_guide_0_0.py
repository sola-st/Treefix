import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def assertDatasetProduces(self, ds, expected_output): # pragma: no cover
        iterator = iter(ds) # pragma: no cover
        produced = list(iterator) # pragma: no cover
        assert produced == expected_output, f"Expected {expected_output}, but got {produced}" # pragma: no cover
mock_test_instance = MockTest() # pragma: no cover
self = mock_test_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
