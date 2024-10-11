import io as io_mock # pragma: no cover

io = type("Mock", (object,), {"save": lambda dataset, path: None, "load": lambda path, spec: dataset_ops.Dataset.range(42)})() # pragma: no cover
self = type("Mock", (object,), {"_test_dir": "/tmp/test", "assertEqual": lambda x, y: None, "evaluate": lambda ds: 42})() # pragma: no cover

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
