# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Row sequence tensor values must not be negative.*"):
    y = nn_ops.gen_nn_ops.fractional_avg_pool_grad(
        orig_input_tensor_shape=[2, 2, 2, 2],
        out_backprop=[[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11,
                                                                    12]]]],
        row_pooling_sequence=[-10, 1, 2, 3],
        col_pooling_sequence=[1, 2, 3, 4],
        overlapping=True)

    self.evaluate(y)
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"Column sequence tensor values must not be negative.*"):
        z = nn_ops.gen_nn_ops.fractional_avg_pool_grad(
            orig_input_tensor_shape=[2, 2, 2, 2],
            out_backprop=[[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11,
                                                                        12]]]],
            row_pooling_sequence=[10, 1, 2, 3],
            col_pooling_sequence=[1, 2, -3, 4],
            overlapping=True)

        self.evaluate(z)
