# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
assert in_depth % num_groups == 0 and out_depth % num_groups == 0
input_shape = [batch, input_rows, input_cols, in_depth]
filter_shape = [filter_rows, filter_cols, in_depth // num_groups, out_depth]
# TODO(yangke): re-factor the computation of output shape.
if padding == "VALID":
    output_rows = (input_rows - filter_rows + stride_rows) // stride_rows
    output_cols = (input_cols - filter_cols + stride_cols) // stride_cols
elif padding == "SAME":
    output_rows = (input_rows + stride_rows - 1) // stride_rows
    output_cols = (input_cols + stride_cols - 1) // stride_cols
else:
    self.assertIsInstance(padding, (list, tuple))
    output_rows = (input_rows + padding[1][0] + padding[1][1] - filter_rows +
                   stride_rows) // stride_rows
    output_cols = (input_cols + padding[2][0] + padding[2][1] - filter_cols +
                   stride_cols) // stride_cols
output_shape = [batch, output_rows, output_cols, out_depth]
input_size = 1
for x in input_shape:
    input_size *= x
filter_size = 1
for x in filter_shape:
    filter_size *= x
input_data = [x * 1.0 / input_size for x in range(0, input_size)]
filter_data = [x * 1.0 / filter_size for x in range(0, filter_size)]
# Conv2DGrad functions are not compiled for double due to
# a problem in the way Eigen's Conv2DGrad works for double.
# So we disable the DOUBLE path.  We should re-enable this
# when double support returns for CPU and/or GPU.
for dtype in self._DtypesToTest(use_gpu=use_gpu):
    with self.cached_session(use_gpu=use_gpu):
        input_tensor = constant_op.constant(
            input_data, shape=input_shape, dtype=dtype, name="input")
        filter_tensor = constant_op.constant(
            filter_data, shape=filter_shape, dtype=dtype, name="filter")
        strides = [1, stride_rows, stride_cols, 1]
        new_padding = padding
        if data_format == "NCHW":
            new_input_tensor = test_util.NHWCToNCHW(input_tensor)
            strides = test_util.NHWCToNCHW(strides)
            if isinstance(padding, (list, tuple)):
                new_padding = test_util.NHWCToNCHW(padding)
        else:
            new_input_tensor = input_tensor
        conv = nn_ops.conv2d(
            new_input_tensor,
            filter_tensor,
            strides,
            new_padding,
            data_format=data_format,
            name="conv")
        if data_format == "NCHW":
            conv = test_util.NCHWToNHWC(conv)
        self.assertEqual(output_shape, conv.get_shape())
        if test_input:
            jacob_t, jacob_n = gradient_checker.compute_gradient(input_tensor,
                                                                 input_shape,
                                                                 conv,
                                                                 output_shape)
        else:
            jacob_t, jacob_n = gradient_checker.compute_gradient(filter_tensor,
                                                                 filter_shape,
                                                                 conv,
                                                                 output_shape)
        if dtype == dtypes.float32:
            reference_jacob_t = jacob_t
            err = np.fabs(jacob_t - jacob_n).max()
        else:
            # Compare fp16/bf16 theoretical gradients to fp32 gradients,
            # since fp16/bf16 numerical gradients are too imprecise.
            err = np.fabs(jacob_t - reference_jacob_t).max()

        tf_logging.debug("conv_2d gradient error = %s", err)
        self.assertLess(err, max_err)
