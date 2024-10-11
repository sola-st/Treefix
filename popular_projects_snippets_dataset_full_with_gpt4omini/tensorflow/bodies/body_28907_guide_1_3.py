class MockTestCase:  # A mock test case class to simulate assertion functionality # pragma: no cover
    def assertDatasetProduces(self, ds, expected):  # Method to check dataset output # pragma: no cover
        output = list(ds.as_numpy_iterator())  # Convert dataset to a list # pragma: no cover
        assert output == expected, f'Expected {expected}, but got {output}' # pragma: no cover
self = MockTestCase()  # Create an instance of MockTestCase # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
