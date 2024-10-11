self = type('Mock', (object,), {'assertDatasetProduces': lambda ds, expected:None})() # pragma: no cover

from unittest import TestCase # pragma: no cover

self = type('MockTestCase', (TestCase,), {'assertDatasetProduces': lambda self, ds, expected: print('Assertion called with dataset:', ds, 'and expected:', expected)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
