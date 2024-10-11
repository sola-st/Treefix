# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
del sess
del output_shape

const_input_ops = [
    constant_op.constant(i, dtype=input_dtype) for i in input_values
]
exit(gen_tpu_ops.xla_concat_nd(const_input_ops, num_concats, paddings))
