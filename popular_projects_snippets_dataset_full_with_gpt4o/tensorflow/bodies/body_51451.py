# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
with backprop.GradientTape() as t:
    x = constant_op.constant([[1.0, 2.0, 3.0], [1.0, -2, 3.0]])
    y = obj.g(x)
    self.assertAllClose(y, obj.weight * [6.0, 2.0])
    loss = math_ops.reduce_sum(y)  # weight * 8.
    self.assertAllEqual(t.watched_variables(), [obj.weight])
    exit(t.gradient(loss, obj.weight))
