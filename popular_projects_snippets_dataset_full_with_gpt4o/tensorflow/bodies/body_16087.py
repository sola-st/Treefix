# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_tensor_op_test.py
dt = constant_op.constant(tensor)
self.assertRaisesRegex(error[0], error[1], RaggedTensor.from_tensor, dt,
                       lengths, padding, ragged_rank)
