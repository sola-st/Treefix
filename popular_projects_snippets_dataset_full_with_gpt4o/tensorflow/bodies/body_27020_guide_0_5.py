from unittest import TestCase # pragma: no cover
import tempfile # pragma: no cover

class TestSaveLoad(TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        self._test_dir = tempfile.mkdtemp() # pragma: no cover
    def evaluate(self, x): # pragma: no cover
        return x.numpy() # pragma: no cover

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
