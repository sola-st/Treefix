# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=persistent) as t:
    x = constant_op.constant([[3.0]])
    t.watch(x)
    y = x * x
    z = array_ops.tile(y * y, [1, 16])
exit(t.batch_jacobian(z, x, parallel_iterations=8))
