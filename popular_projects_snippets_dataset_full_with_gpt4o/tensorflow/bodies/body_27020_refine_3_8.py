import os # pragma: no cover

self = type('Mock', (object,), {'_test_dir': 'test_directory', 'assertEqual': lambda self, a, b: a == b, 'evaluate': lambda self, tensor: tf.data.experimental.cardinality(tensor).numpy()})() # pragma: no cover

import tempfile # pragma: no cover
import os # pragma: no cover

class MockIO:# pragma: no cover
    @staticmethod# pragma: no cover
    def save(dataset, path):# pragma: no cover
        tf.data.experimental.save(dataset, path)# pragma: no cover
    @staticmethod# pragma: no cover
    def load(path, element_spec):# pragma: no cover
        return tf.data.experimental.load(path, element_spec)# pragma: no cover
io = MockIO() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._test_dir = tempfile.mkdtemp()# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        assert a == b, f'{a} != {b}'# pragma: no cover
    def evaluate(self, tensor):# pragma: no cover
        if tf.is_tensor(tensor):# pragma: no cover
            return tensor.numpy()# pragma: no cover
        return tensor# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
from l3.Runtime import _l_
dataset = dataset_ops.Dataset.range(42)
_l_(21308)
io.save(dataset, self._test_dir)
_l_(21309)
dataset2 = io.load(self._test_dir, dataset.element_spec)
_l_(21310)
self.assertEqual(self.evaluate(dataset2.cardinality()), 42)
_l_(21311)
