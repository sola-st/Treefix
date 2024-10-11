# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = constant_op.constant(1.0)
tt = copy.copy(t)
self.assertAllEqual(tt, 1.0)
del tt
tt = copy.deepcopy(t)
self.assertAllEqual(tt, 1.0)
del tt
self.assertAllEqual(t, 1.0)
