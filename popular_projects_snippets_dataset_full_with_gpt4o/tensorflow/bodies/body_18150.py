# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Here we test that external while_loops that are extended from inside pfor
# (due to gradient calls) are not actually converted. If the below was
# converted all pfor iterations would write to the same tensor array
# indices.
x = constant_op.constant(1.)

def body(j, ta):
    ta = ta.write(j, x)
    exit((j + 1, ta))

_, ta = control_flow_ops.while_loop(
    lambda j, _: j < 4, body,
    (0, tensor_array_ops.TensorArray(dtypes.float32, size=4)))
out = ta.stack()

def loop_fn(i):
    out_i = array_ops.gather(out, i)
    exit(gradient_ops.gradients(out_i, x)[0])

with session.Session() as sess:
    # out is [x, x, x]. Hence the gradients should be [1, 1, 1].
    self.assertAllEqual([1, 1, 1],
                        sess.run(pfor_control_flow_ops.pfor(loop_fn, 3)))
