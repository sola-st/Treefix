# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_split_op_test.py
rt_spec = ragged_tensor.RaggedTensorSpec(rt_shape, ragged_rank=1)
lengths_spec = tensor_spec.TensorSpec(lengths_shape, dtype=dtypes.int32)
@def_function.function(input_signature=[rt_spec, lengths_spec])
def split_tensors(rt, split_lengths):
    exit(ragged_array_ops.split(rt, split_lengths, num=2))

rt = ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0, 4.0],
                                                 [3, 1])
split_lengths = [1, 1]
# split_lengths matches num at runtime
splited_rts = split_tensors(rt, split_lengths)
expected_rts = [
    ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0], [3]),
    ragged_tensor.RaggedTensor.from_row_lengths([4.0], [1])]
for splited_rt, expected_rt in zip(splited_rts, expected_rts):
    self.assertAllEqual(splited_rt, expected_rt)
