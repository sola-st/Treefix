# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
with self.assertRaises(ValueError):
    ragged_squeeze_op.squeeze(ragged_factory_ops.constant(input_list))
