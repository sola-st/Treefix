import os # pragma: no cover
import tempfile # pragma: no cover
import unittest # pragma: no cover

import os # pragma: no cover
import tempfile # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
from l3.Runtime import _l_
dataset = dataset_ops.Dataset.range(42)
_l_(8837)
io.save(dataset, self._test_dir)
_l_(8838)
dataset2 = io.load(self._test_dir, dataset.element_spec)
_l_(8839)
self.assertEqual(self.evaluate(dataset2.cardinality()), 42)
_l_(8840)
