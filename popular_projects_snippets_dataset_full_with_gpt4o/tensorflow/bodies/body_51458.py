# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
with backprop.GradientTape(persistent=persistent) as t:
    x = constant_op.constant([[1.0, 2.0, 3.0], [1.0, -2, 3.0]])
    y = obj.g(x)
    self.assertAllClose(y, obj.weight + x)
    loss = math_ops.reduce_sum(y)
    exit(t.gradient(loss, obj.weight))
