# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
tensor = array_ops.zeros(input_shape)
ragged_from_tensor = RaggedTensor.from_tensor(tensor, ragged_rank=2)
recovered_tensor = ragged_from_tensor.to_tensor(shape=to_tensor_shape)
self.assertAllEqual(tensor.shape.as_list(), expected_shape)
self.assertAllEqual(ragged_from_tensor.shape.as_list(), expected_shape)
self.assertAllEqual(recovered_tensor.shape.as_list(), expected_shape)
