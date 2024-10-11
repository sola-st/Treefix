# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
rt = ragged_squeeze_op.squeeze(
    ragged_factory_ops.constant(input_list), squeeze_ranks)
dt = array_ops.squeeze(constant_op.constant(input_list), squeeze_ranks)
self.assertAllEqual(ragged_conversion_ops.to_tensor(rt), dt)
