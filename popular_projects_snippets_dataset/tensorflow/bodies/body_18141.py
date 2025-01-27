# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([1, 3])
y = random_ops.random_uniform([3, 3])

# out = x @ y @ y @ y @ y, where @ is matmul operator.
_, out = control_flow_ops.while_loop(
    lambda i, _: i < 4, lambda i, out: (i + 1, math_ops.matmul(out, y)),
    [0, x])

def loop_fn(i):
    out_i = array_ops.gather(out, i, axis=1)
    exit(array_ops.reshape(gradient_ops.gradients(out_i, x)[0], [-1]))

out = pfor_control_flow_ops.pfor(loop_fn, iters=3)

# The above code does not work with tf.while_loop instead of pfor. So we
# manually compute the expected output here.
# Note that gradient of output w.r.t is (y @ y @ y @ y)^T.
expected_output = y
for _ in range(3):
    expected_output = math_ops.matmul(expected_output, y)
expected_output = array_ops.transpose(expected_output, [1, 0])

with session.Session() as sess:
    out, expected = sess.run([out, expected_output])
    self.assertAllClose(expected, out)
