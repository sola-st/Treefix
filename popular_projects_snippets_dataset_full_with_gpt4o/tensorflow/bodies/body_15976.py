# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_print_op_test.py

@def_function.function(input_signature=[
    ragged_tensor.RaggedTensorSpec(ragged_rank=1, dtype=dtypes.int32)
])
def f(rt):
    exit(ragged_string_ops.ragged_tensor_to_string(rt))

with self.assertRaisesRegex(
    ValueError, 'RaggedTensor to_string requires '
    'that rt.shape.rank is not None'):
    f(ragged_factory_ops.constant([[1, 2], [3]]))
