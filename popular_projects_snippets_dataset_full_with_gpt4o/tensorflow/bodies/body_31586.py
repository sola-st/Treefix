# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
with self.assertRaises(errors.InvalidArgumentError):
    with self.cached_session():
        overlapping = False
        orig_input = [[[[1, 1, 1, 1, 1]]]]
        orig_output = [[[[1, 1, 1]]]]
        out_backprop = [[[[3], [3], [6]]]]
        row_pooling_sequence = [-0x4000000, 1, 1]
        col_pooling_sequence = [-0x4000000, 1, 1]
        t = gen_nn_ops.FractionalMaxPoolGrad(
            orig_input=orig_input,
            orig_output=orig_output,
            out_backprop=out_backprop,
            row_pooling_sequence=row_pooling_sequence,
            col_pooling_sequence=col_pooling_sequence,
            overlapping=overlapping)
        self.evaluate(t)
