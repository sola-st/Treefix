import os # pragma: no cover
import tempfile # pragma: no cover
import unittest # pragma: no cover

io = type('Mock', (object,), { 'save': lambda ds, path: tf.data.experimental.save(ds, path), 'load': lambda path, spec: tf.data.experimental.load(path, spec) }) # pragma: no cover
self = type('Mock', (unittest.TestCase,), { '_test_dir': tempfile.mkdtemp(), 'assertEqual': unittest.TestCase().assertEqual, 'evaluate': lambda self, x: x.numpy() })() # pragma: no cover

import os # pragma: no cover
import tempfile # pragma: no cover
import unittest # pragma: no cover

io = type('Mock', (object,), { 'save': lambda ds, path: tf.data.experimental.save(ds, path), 'load': lambda path, spec: tf.data.experimental.load(path, spec) })() # pragma: no cover
self = type('Mock', (unittest.TestCase,), { '_test_dir': tempfile.mkdtemp(), 'assertEqual': unittest.TestCase().assertEqual, 'evaluate': lambda self, x: x })() # pragma: no cover

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
