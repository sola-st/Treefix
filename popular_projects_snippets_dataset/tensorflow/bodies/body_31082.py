# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    with self.cached_session() as _:
        overlapping = True
        orig_input_tensor_shape = constant_op.constant(
            -1879048192, shape=[4], dtype=dtypes.int64)
        out_backprop = constant_op.constant([],
                                            shape=[0, 0, 0, 0],
                                            dtype=dtypes.float64)
        row_pooling_sequence = constant_op.constant(
            1, shape=[4], dtype=dtypes.int64)
        col_pooling_sequence = constant_op.constant(
            1, shape=[4], dtype=dtypes.int64)
        t = gen_nn_ops.fractional_avg_pool_grad(
            orig_input_tensor_shape=orig_input_tensor_shape,
            out_backprop=out_backprop,
            row_pooling_sequence=row_pooling_sequence,
            col_pooling_sequence=col_pooling_sequence,
            overlapping=overlapping)
        self.evaluate(t)
