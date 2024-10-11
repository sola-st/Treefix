# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
with self.assertRaises(errors.InvalidArgumentError):
    with self.cached_session():
        overlapping = True
        orig_input = constant_op.constant(
            .453409232, shape=[1, 7, 13, 1], dtype=dtypes.float32)
        orig_output = constant_op.constant(
            .453409232, shape=[1, 7, 13, 1], dtype=dtypes.float32)
        out_backprop = constant_op.constant(
            .453409232, shape=[1, 7, 13, 1], dtype=dtypes.float32)
        row_pooling_sequence = constant_op.constant(
            0, shape=[5], dtype=dtypes.int64)
        col_pooling_sequence = constant_op.constant(
            0, shape=[5], dtype=dtypes.int64)
        t = gen_nn_ops.FractionalMaxPoolGrad(
            orig_input=orig_input,
            orig_output=orig_output,
            out_backprop=out_backprop,
            row_pooling_sequence=row_pooling_sequence,
            col_pooling_sequence=col_pooling_sequence,
            overlapping=overlapping)
        self.evaluate(t)
