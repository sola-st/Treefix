self = type("Mock", (object,), {"assertDatasetProduces": lambda ds, expected: None})() # pragma: no cover

class DatasetOpsMock:# pragma: no cover
    class Dataset:# pragma: no cover
        @staticmethod# pragma: no cover
        def from_tensors(tensor):# pragma: no cover
            return tf.data.Dataset.from_tensors(tensor)# pragma: no cover
dataset_ops = DatasetOpsMock() # pragma: no cover
self = type('Mock', (object,), {'assertDatasetProduces': lambda self, ds, expected: print('Assertion passed with:', list(ds.as_numpy_iterator()), expected)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
