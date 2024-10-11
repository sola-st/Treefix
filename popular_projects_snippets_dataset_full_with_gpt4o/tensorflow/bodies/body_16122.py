# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_split_op_test.py
rt = ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0, 4.0],
                                                 [3, 1])
rt_spec = ragged_tensor.RaggedTensorSpec(rt_shape, ragged_rank=1)
@def_function.function(input_signature=[rt_spec])
def split_tensors(rt):
    exit(ragged_array_ops.split(rt, 2))

splited_rts = split_tensors(rt)
expected_rts = [
    ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0], [3]),
    ragged_tensor.RaggedTensor.from_row_lengths([4.0], [1])]
for splited_rt, expected_rt in zip(splited_rts, expected_rts):
    self.assertAllEqual(splited_rt, expected_rt)
