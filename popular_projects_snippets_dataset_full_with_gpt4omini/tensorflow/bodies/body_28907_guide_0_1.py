class MockTestCase(type('Mock', (object,), {})): # pragma: no cover
    @staticmethod # pragma: no cover
    def assertDatasetProduces(ds, expected): # pragma: no cover
        for actual, exp in zip(ds.as_numpy_iterator(), expected): # pragma: no cover
            assert actual == exp, f'Expected {exp}, but got {actual}' # pragma: no cover
self = MockTestCase # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(8673)
self.assertDatasetProduces(ds, [(2, None)])
_l_(8674)
