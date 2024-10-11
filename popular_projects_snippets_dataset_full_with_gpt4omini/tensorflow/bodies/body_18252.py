# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Vmap should be able to handle ragged Tensors as long as they're not
# *actually* ragged.
ragged = ragged_tensor.RaggedTensor.from_uniform_row_length(
    ragged_tensor.RaggedTensor.from_row_lengths(
        values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        row_lengths=[3, 3, 3, 3]),
    uniform_row_length=2)  # Overall shape [2, 2, 3].
self.assertAllEqual(
    pfor_control_flow_ops.vectorized_map(
        lambda x: x.to_tensor(shape=[2, 3]), ragged),
    ragged.to_tensor(shape=[2, 2, 3]))
