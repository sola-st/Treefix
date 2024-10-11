import tempfile # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        # Creating a temporary directory for testing # pragma: no cover
        self._test_dir = tempfile.mkdtemp() # pragma: no cover
    def evaluate(self, val): # pragma: no cover
        # Evaluating tensors if necessary # pragma: no cover
        return val.numpy() if isinstance(val, tf.Tensor) else val # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        # Custom assertion method # pragma: no cover
        assert a == b, f'{a} != {b}' # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover

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
