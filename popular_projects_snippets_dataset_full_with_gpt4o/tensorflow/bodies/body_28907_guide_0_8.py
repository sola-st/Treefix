import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def assertDatasetProduces(self, dataset, expected_output): # pragma: no cover
        itr = iter(dataset) # pragma: no cover
        produced_output = next(itr).numpy() # pragma: no cover
        assert produced_output == expected_output, f'Expected {expected_output} but got {produced_output}' # pragma: no cover
 # pragma: no cover
self = type('Mock', (MockTest,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
