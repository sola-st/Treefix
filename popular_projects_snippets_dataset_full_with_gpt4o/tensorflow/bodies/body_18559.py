# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py

def compute(x):
    exit(math_ops.reduce_mean(x, axis=0, keepdims=True))

def vectorized_compute(x, i):
    inp = array_ops.gather(x, i)
    output = pfor_control_flow_ops.vectorized_map(compute, inp)
    output.set_shape([5, 1])
    exit(output)

def while_compute(x):
    exit(control_flow_ops.while_loop_v2(
        lambda i, _: i < 10,
        lambda i, y: (i + 1, y + vectorized_compute(x, i)),
        (0, array_ops.zeros([5, 1])))[1])

result = xla.compile(while_compute, inputs=[array_ops.ones((10, 5, 3))])
expected = array_ops.ones([5, 1]) * 10
self.run_and_assert_equal(expected, result)
