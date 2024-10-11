# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
no_rank_spec = ragged_tensor.RaggedTensorSpec(None, dtypes.int32, 1)
rank_only_spec = ragged_tensor.RaggedTensorSpec([None, None], dtypes.int32,
                                                1)

matmul_no_rank_for_a = def_function.function(
    input_signature=[rank_only_spec, no_rank_spec])(
        ragged_math_ops.matmul)
matmul_no_rank_for_b = def_function.function(
    input_signature=[no_rank_spec, rank_only_spec])(
        ragged_math_ops.matmul)
matmul_no_rank_for_a_or_b = def_function.function(
    input_signature=[no_rank_spec, no_rank_spec])(
        ragged_math_ops.matmul)

a = ragged_factory_ops.constant([[1, 2]])
b = ragged_factory_ops.constant([[3], [4]])
self.assertAllEqual(matmul_no_rank_for_a(a, b), [[11]])
self.assertAllEqual(matmul_no_rank_for_b(a, b), [[11]])
with self.assertRaisesRegex(
    ValueError, 'matmul requires at least one input to have known '
    'rank if either input is ragged.'):
    matmul_no_rank_for_a_or_b(a, b)
