# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
with ops.device("CPU"):
    t = constant_op.constant([0.0])
    t._numpy()[0] = 42.0
    self.assertAllClose(t, constant_op.constant([42.0]))
