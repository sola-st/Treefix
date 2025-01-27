# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_split_op_test.py
rt_spec = ragged_tensor.RaggedTensorSpec(rt_shape, ragged_rank=1)
split_lengths_spec = tensor_spec.TensorSpec(lengths_shape,
                                            dtype=dtypes.int32)
@def_function.function(input_signature=[rt_spec, split_lengths_spec])
def split_tensors(rt, split_lengths):
    exit(ragged_array_ops.split(rt, split_lengths, axis=axis, num=num))

rt = ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0, 4.0],
                                                 [3, 1])
with self.assertRaisesRegex(exception, message):
    self.evaluate(split_tensors(rt=rt, split_lengths=lengths))
