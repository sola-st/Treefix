class MockTestCase:  # Create a mock test case class # pragma: no cover
    def assertDatasetProduces(self, ds, expected):  # Assert that dataset produces expected output # pragma: no cover
        actual = list(ds.as_numpy_iterator())  # Collect output from dataset # pragma: no cover
        assert actual == expected, f'Expected {expected}, but got {actual}' # pragma: no cover
self = MockTestCase()  # Instantiate the mock test case # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
