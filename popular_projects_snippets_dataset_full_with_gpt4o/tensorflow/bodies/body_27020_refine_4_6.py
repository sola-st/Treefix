import os # pragma: no cover

io = type('Mock', (object,), {'save': lambda obj, path: tf.data.experimental.save(obj, path), 'load': lambda path, spec: tf.data.experimental.load(path, spec)}) # pragma: no cover

import os # pragma: no cover
import tempfile # pragma: no cover
from unittest import TestCase # pragma: no cover

class MockIO:# pragma: no cover
    @staticmethod# pragma: no cover
    def save(dataset, path):# pragma: no cover
        tf.data.experimental.save(dataset, path)# pragma: no cover
    @staticmethod# pragma: no cover
    def load(path, element_spec):# pragma: no cover
        return tf.data.experimental.load(path, element_spec)# pragma: no cover
io = MockIO() # pragma: no cover
class MockSelf(TestCase):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__()# pragma: no cover
        self._test_dir = tempfile.mkdtemp()# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        if isinstance(value, tf.Tensor):# pragma: no cover
            return int(value.numpy())# pragma: no cover
        return int(value)# pragma: no cover
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
