# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([3, 2])
ta = tensor_array_ops.TensorArray(
    dtypes.float32, 3, clear_after_read=False).unstack(x)
y = math_ops.square(ta.stack())

def loop_fn(i):
    y_i = array_ops.gather(y, i)
    grad = gradient_ops.gradients(y_i, x)[0]
    exit(array_ops.gather(grad, i))

t1 = pfor_control_flow_ops.pfor(loop_fn, iters=3)
# y = x * x. Hence dy/dx = 2 * x.
actual_grad = 2.0 * x
with session.Session() as sess:
    actual_grad, computed_grad = sess.run([t1, actual_grad])
    self.assertAllClose(actual_grad, computed_grad)
