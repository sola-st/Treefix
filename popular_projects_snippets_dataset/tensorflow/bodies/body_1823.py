# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
del sess

const_input_op = constant_op.constant(input_value, dtype=input_dtype)
exit(gen_tpu_ops.xla_split_nd(
    const_input_op, num_outputs, num_splits, paddings=paddings))
