import os # pragma: no cover

class MockEvaluate: # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._test_dir = os.path.join(os.getcwd(), 'test_dir') # pragma: no cover
os.makedirs(self._test_dir, exist_ok=True) # pragma: no cover
self.evaluate = MockEvaluate().evaluate # pragma: no cover

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
