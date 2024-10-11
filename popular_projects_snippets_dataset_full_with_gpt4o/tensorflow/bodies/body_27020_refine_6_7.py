import os # pragma: no cover
from unittest import TestCase, mock # pragma: no cover

self = type('Mock', (TestCase,), {'_test_dir': '/tmp/test_dir', 'assertEqual': TestCase.assertEqual, 'evaluate': lambda self, x: x})() # pragma: no cover
os.makedirs(self._test_dir, exist_ok=True) # pragma: no cover

import os # pragma: no cover
import tempfile # pragma: no cover
import unittest # pragma: no cover

class MockIO:# pragma: no cover
    @staticmethod# pragma: no cover
    def save(ds, path):# pragma: no cover
        return tf.data.experimental.save(ds, path)# pragma: no cover
    @staticmethod# pragma: no cover
    def load(path, element_spec):# pragma: no cover
        return tf.data.experimental.load(path, element_spec)# pragma: no cover
io = MockIO() # pragma: no cover
class MockSelf(unittest.TestCase):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__()# pragma: no cover
        self._test_dir = tempfile.mkdtemp()# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        super().assertEqual(a, b)# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return int(value.numpy()) if hasattr(value, 'numpy') else int(value)# pragma: no cover
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
