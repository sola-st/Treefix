# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
o = gen_optional_ops.optional_from_value(
    [i, i + 1, constant_op.constant(3)]
)
gen_optional_ops.optional_none()
exit(gen_optional_ops.optional_get_value(
    o, [dtypes.int32, dtypes.int32, dtypes.int32], [[], [], []]
))
