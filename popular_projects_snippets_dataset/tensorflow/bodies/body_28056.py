# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
int_placeholder = array_ops.placeholder(dtypes.int32)
float_placeholder = array_ops.placeholder(dtypes.float32)
string_placeholder = array_ops.placeholder(dtypes.string)
input_dataset = dataset_ops.Dataset.from_tensors(
    (int_placeholder, float_placeholder, string_placeholder))

# Test different ways of specifying the `padded_shapes` argument.
dynamic_padding_from_tensor_shapes = input_dataset.padded_batch(
    32,
    padded_shapes=(tensor_shape.TensorShape([None]),
                   tensor_shape.TensorShape([None, None]),
                   tensor_shape.TensorShape([37])))
dynamic_padding_from_lists = input_dataset.padded_batch(
    32, padded_shapes=([None], [None, None], [37]))
dynamic_padding_from_lists_with_minus_one = input_dataset.padded_batch(
    32, padded_shapes=([-1], [-1, -1], [37]))
dynamic_padding_from_tensors = input_dataset.padded_batch(
    32,
    padded_shapes=(constant_op.constant([-1], dtype=dtypes.int64),
                   constant_op.constant([-1, -1], dtype=dtypes.int64),
                   constant_op.constant([37], dtype=dtypes.int64)))

for dataset in [
    dynamic_padding_from_tensor_shapes, dynamic_padding_from_lists,
    dynamic_padding_from_lists_with_minus_one, dynamic_padding_from_tensors
]:
    dataset_output_shapes = dataset_ops.get_legacy_output_shapes(dataset)
    self.assertEqual([None, None], dataset_output_shapes[0].as_list())
    self.assertEqual([None, None, None], dataset_output_shapes[1].as_list())
    self.assertEqual([None, 37], dataset_output_shapes[2].as_list())
