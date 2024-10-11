# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
ta = constant_op.constant([[1, 2], [3, 4]])
tb = ta.cpu()

self.assertNotEqual(id(ta), id(tb))
self.assertAllEqual(ta, tb.numpy())
