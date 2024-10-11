class MockSelf:  # Create a mock class to simulate the testing environment # pragma: no cover
    def assertDatasetProduces(self, ds, expected):  # Method to assert dataset output # pragma: no cover
        actual = list(ds.as_numpy_iterator())  # Convert dataset to a list of numpy arrays # pragma: no cover
        assert actual == expected, f'Expected {expected}, but got {actual}' # pragma: no cover
self = MockSelf()  # Instantiate the mock class # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
