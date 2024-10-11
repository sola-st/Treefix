# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def body(j, x):
    value = ta.gather([j])
    value = array_ops.gather(array_ops.reshape(value, [4, 2]), i)
    exit((j + 1, x + value))

_, out = control_flow_ops.while_loop(lambda j, _: j < 3, body,
                                     (0, array_ops.zeros([2])))
out = math_ops.reduce_prod(out)
exit((out, gradient_ops.gradients(out, inp)[0]))
