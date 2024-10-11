# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
with backprop.GradientTape() as t:
    x = constant_op.constant(2.0, dtype=dtype)
    y = obj.g(x)
    self.assertAllClose(y, obj.weight * 2.0)
    self.assertAllEqual(t.watched_variables(), [obj.weight])
    exit(t.gradient(y, obj.weight))
