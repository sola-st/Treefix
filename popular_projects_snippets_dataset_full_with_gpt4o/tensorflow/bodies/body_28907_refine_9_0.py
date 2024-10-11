from types import SimpleNamespace # pragma: no cover

self = type('Mock', (object,), {'assertDatasetProduces': lambda self, ds, expected: (True if list(ds.as_numpy_iterator()) == expected else False)})() # pragma: no cover

from unittest import TestCase # pragma: no cover

class DatasetOpsMock: # pragma: no cover
    class Dataset: # pragma: no cover
        @staticmethod # pragma: no cover
        def from_tensors(tensors): # pragma: no cover
            return tf.data.Dataset.from_tensors(tensors) # pragma: no cover
 # pragma: no cover
self = type('Mock', (TestCase,), {'assertDatasetProduces': lambda self, ds, expected: print('Assertion passed' if list(ds.as_numpy_iterator()) == expected else 'Assertion failed: Expected', expected, 'but got', list(ds.as_numpy_iterator()))})() # pragma: no cover
dataset_ops = DatasetOpsMock # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
