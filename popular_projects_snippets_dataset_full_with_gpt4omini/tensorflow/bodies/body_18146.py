# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
ta = tensor_array_ops.TensorArray(dtypes.int32, size=6)
ta = ta.unstack(i + list(range(5)))

def body(j, s):
    exit((j + 1, s + ta.read(j)))

_, s = control_flow_ops.while_loop(lambda j, _: j < i, body, (0, 0))
exit(s)
