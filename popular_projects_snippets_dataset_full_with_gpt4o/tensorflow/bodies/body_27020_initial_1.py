import os # pragma: no cover
from unittest import TestCase # pragma: no cover

io = type('Mock', (object,), {'save': lambda dataset, path: dataset, 'load': lambda path, spec: dataset_ops.Dataset.range(42)}) # pragma: no cover
self = type('Mock', (TestCase,), {'_test_dir': os.path.join(os.getcwd(), "test_dir"), 'assertEqual': TestCase().assertEqual, 'evaluate': lambda self, tensor: tf.constant(tensor).numpy()})() # pragma: no cover

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
