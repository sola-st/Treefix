# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
with self.assertRaises(TypeError):
    tensor_ranks = constant_op.constant(squeeze_ranks)
    ragged_squeeze_op.squeeze(
        ragged_factory_ops.constant(input_list), tensor_ranks)
