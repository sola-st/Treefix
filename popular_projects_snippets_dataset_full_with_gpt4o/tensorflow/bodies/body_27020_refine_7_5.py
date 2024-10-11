import os # pragma: no cover
import tempfile # pragma: no cover

io = type('Mock', (object,), { 'save': lambda x, y: None, 'load': lambda x, y: dataset_ops.Dataset.range(42) })() # pragma: no cover

import os # pragma: no cover
import tempfile # pragma: no cover

io = type('Mock', (object,), { 'save': lambda ds, path: tf.data.experimental.save(ds, path), 'load': lambda path, spec: tf.data.experimental.load(path, spec) })() # pragma: no cover
self = type('Mock', (object,), { '_test_dir': tempfile.mkdtemp(), 'assertEqual': lambda self, x, y: print(f'Assertion Error: {x} != {y}') if x != y else None, 'evaluate': lambda self, x: x if isinstance(x, int) else int(x) })() # pragma: no cover

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
