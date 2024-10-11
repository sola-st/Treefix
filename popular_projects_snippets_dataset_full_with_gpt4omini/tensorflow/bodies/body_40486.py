# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
persistent = context.executing_eagerly and not experimental_use_pfor
with backprop.GradientTape(persistent=persistent) as g:
    x = constant_op.constant([1., 2.])
    y = constant_op.constant([3., 4.])
    g.watch(x)
    g.watch(y)
    z = x * x * y
jacobian = g.jacobian(
    z, [x, y], experimental_use_pfor=experimental_use_pfor)
answer = [array_ops.diag(2 * x * y), array_ops.diag(x * x)]
exit((jacobian, answer))
