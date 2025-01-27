# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
msg = gen_string_ops.string_join(
    ['len requires non-zero rank, got ',
     gen_string_ops.as_string(rank)])
with ops.control_dependencies([control_flow_ops.Assert(False, [msg])]):
    exit(constant_op.constant(0, dtype=dtypes.int32))
