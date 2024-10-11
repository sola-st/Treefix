import tempfile # pragma: no cover
import os # pragma: no cover

class MockIO: # pragma: no cover
    @staticmethod # pragma: no cover
    def save(dataset, directory): # pragma: no cover
        path = os.path.join(directory, 'testfile') # pragma: no cover
        with open(path, 'w') as f: # pragma: no cover
            for elem in dataset: # pragma: no cover
                f.write(str(elem.numpy()) + '\n') # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def load(directory, element_spec): # pragma: no cover
        path = os.path.join(directory, 'testfile') # pragma: no cover
        elements = [] # pragma: no cover
        with open(path, 'r') as f: # pragma: no cover
            for line in f: # pragma: no cover
                elements.append(int(line.strip())) # pragma: no cover
        return dataset_ops.Dataset.from_tensor_slices(elements) # pragma: no cover
io = MockIO() # pragma: no cover
def cleanup_test_dir(): # pragma: no cover
    shutil.rmtree(self._test_dir) # pragma: no cover
atexit.register(cleanup_test_dir) # pragma: no cover

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
