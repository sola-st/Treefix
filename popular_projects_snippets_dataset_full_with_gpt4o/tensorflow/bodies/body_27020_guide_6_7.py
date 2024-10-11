import os # pragma: no cover
import shutil # pragma: no cover

class MockTest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._test_dir = os.path.join(os.getcwd(), 'test_data') # pragma: no cover
        if not os.path.exists(self._test_dir): # pragma: no cover
            os.makedirs(self._test_dir) # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() if tf.is_tensor(tensor) else tensor # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b, f'{a} != {b}' # pragma: no cover
    def cleanup(self): # pragma: no cover
        if os.path.exists(self._test_dir): # pragma: no cover
            shutil.rmtree(self._test_dir) # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover
atexit.register(self.cleanup) # pragma: no cover

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
