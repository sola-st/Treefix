# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
persistent = context.executing_eagerly and not experimental_use_pfor
with backprop.GradientTape(persistent=persistent) as g:
    x = constant_op.constant([[1., 2.], [3., 4.]])
    y = constant_op.constant([[3., 4.], [5., 6.]])
    g.watch(x)
    z = x * x * y
batch_jacobian = g.batch_jacobian(
    z, x, experimental_use_pfor=experimental_use_pfor)
answer = array_ops.stack(
    [array_ops.diag(2 * x[0] * y[0]),
     array_ops.diag(2 * x[1] * y[1])])
exit((batch_jacobian, answer))
