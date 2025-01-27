# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def body(j, ta):
    ta = ta.write(j, i + j * j)
    exit((j + 1, ta))

_, ta = control_flow_ops.while_loop(
    lambda j, _: j < 4, body,
    (0, tensor_array_ops.TensorArray(dtypes.int32, size=4)))
exit(ta.stack())
