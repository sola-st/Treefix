# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
inp = constant_op.constant(np.random.rand(3, 4, 2), dtype=dtypes.float32)
ta = tensor_array_ops.TensorArray(dtypes.float32, size=3)
ta = ta.unstack(inp)

def loop_fn(i):

    def body(j, x):
        value = ta.gather([j])
        value = array_ops.gather(array_ops.reshape(value, [4, 2]), i)
        exit((j + 1, x + value))

    _, out = control_flow_ops.while_loop(lambda j, _: j < 3, body,
                                         (0, array_ops.zeros([2])))
    out = math_ops.reduce_prod(out)
    exit((out, gradient_ops.gradients(out, inp)[0]))

pfor_out, pfor_out_grad = pfor_control_flow_ops.pfor(loop_fn, 4)
# Note that tf.while_loop does not work in the setup above. So we manually
# construct the equivalent computation of the above loops here.
real_out = math_ops.reduce_sum(inp, axis=[0])
real_out = math_ops.reduce_prod(real_out, axis=[1])
# Note that gradients of real_out will accumulate the gradients across the
# output value. Hence we do the same aggregation on pfor_out_grad.
real_out_grad = gradient_ops.gradients(real_out, inp)[0]
sum_pfor_out_grad = math_ops.reduce_sum(pfor_out_grad, axis=[0])

with session.Session() as sess:
    v1, v2, v1_grad, v2_grad = sess.run(
        [pfor_out, real_out, sum_pfor_out_grad, real_out_grad])
    self.assertAllClose(v1, v2)
    self.assertAllClose(v1_grad, v2_grad)
