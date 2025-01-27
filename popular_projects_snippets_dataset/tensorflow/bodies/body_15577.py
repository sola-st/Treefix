# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op_test.py
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(
        ragged_squeeze_op.squeeze(
            ragged_factory_ops.constant(input_list), squeeze_ranks))
