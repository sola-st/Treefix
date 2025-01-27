# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py

input_planes, input_rows, input_cols = input_shape
filter_planes, filter_rows, filter_cols = filter_shape

input_shape = [batch, input_planes, input_rows, input_cols, in_depth]
filter_shape = [
    filter_planes, filter_rows, filter_cols, in_depth, out_depth
]

if isinstance(stride, collections_abc.Iterable):
    strides = [1] + list(stride) + [1]
else:
    strides = [1, stride, stride, stride, 1]

if padding == "VALID":
    output_planes = int(
        math.ceil((input_planes - filter_planes + 1.0) / strides[1]))
    output_rows = int(
        math.ceil((input_rows - filter_rows + 1.0) / strides[2]))
    output_cols = int(
        math.ceil((input_cols - filter_cols + 1.0) / strides[3]))
else:
    output_planes = int(math.ceil(float(input_planes) / strides[1]))
    output_rows = int(math.ceil(float(input_rows) / strides[2]))
    output_cols = int(math.ceil(float(input_cols) / strides[3]))
output_shape = [batch, output_planes, output_rows, output_cols, out_depth]
input_size = 1
for x in input_shape:
    input_size *= x
filter_size = 1
for x in filter_shape:
    filter_size *= x
input_data = [x * 1.0 / input_size for x in range(0, input_size)]
filter_data = [x * 1.0 / filter_size for x in range(0, filter_size)]

for data_type in self._DtypesToTest(use_gpu=use_gpu):
    # TODO(mjanusz): Modify gradient_checker to also provide max relative
    # error and synchronize the tolerance levels between the tests for forward
    # and backward computations.
    if data_type == dtypes.float64:
        tolerance = 1e-8
    elif data_type == dtypes.float32:
        tolerance = 5e-3
    elif data_type == dtypes.float16:
        tolerance = 5e-3 if test.is_built_with_rocm() else 1e-3
    elif data_type == dtypes.bfloat16:
        tolerance = 1e-2

    with self.cached_session(use_gpu=use_gpu):
        orig_input_tensor = constant_op.constant(
            input_data, shape=input_shape, dtype=data_type, name="input")
        filter_tensor = constant_op.constant(
            filter_data, shape=filter_shape, dtype=data_type, name="filter")

        if data_format == "NCDHW":
            input_tensor = test_util.NHWCToNCHW(orig_input_tensor)
            new_strides = test_util.NHWCToNCHW(strides)
        else:
            input_tensor = orig_input_tensor
            new_strides = strides

        conv = nn_ops.conv3d(
            input_tensor,
            filter_tensor,
            new_strides,
            padding,
            data_format=data_format,
            name="conv")

        if data_format == "NCDHW":
            conv = test_util.NCHWToNHWC(conv)

        self.assertEqual(conv.shape, tensor_shape.TensorShape(output_shape))

        if test_input:
            jacob_t, jacob_n = gradient_checker.compute_gradient(
                orig_input_tensor, input_shape, conv, output_shape)
        else:
            jacob_t, jacob_n = gradient_checker.compute_gradient(
                filter_tensor, filter_shape, conv, output_shape)

        if data_type != dtypes.float16 and data_type != dtypes.bfloat16:
            reference_jacob_t = jacob_t
            err = np.fabs(jacob_t - jacob_n).max()
        else:
            # Compare fp16/bf16 theoretical gradients to fp32 theoretical
            # gradients, since fp16/bf16 numerical gradients are too imprecise.
            err = np.fabs(jacob_t - reference_jacob_t).max()

    print("conv3d gradient error = ", err)
    self.assertLess(err, tolerance)
