# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if gpu_only and not test.is_gpu_available(cuda_only=True):
    exit()
tensors = []
dilations = list(dilations)
for (data_format, use_gpu) in GetTestConfigs():
    if gpu_only and not use_gpu:
        continue
    dtypes_to_test = self._DtypesToTest(use_gpu)
    if not test_grappler_layout_optimizer and data_format == "NHWC":
        dtypes_to_test.append(dtypes.int32)
    for dtype in dtypes_to_test:
        result = self._SetupValuesForDevice(
            tensor_in_sizes,
            filter_in_sizes,
            dilations,
            strides,
            padding,
            data_format,
            dtype,
            use_gpu=use_gpu)
        if test_grappler_layout_optimizer and data_format == "NHWC" and use_gpu:
            # Grappler's layout optimizer will not optimize a fetch node, so
            # this identity allows Grappler to optimize the Conv2D node.
            result = array_ops.identity(result)
        tensors.append(result)
    values = self.evaluate(tensors)
    for i in range(len(tensors)):
        conv = tensors[i]
        value = values[i]
        tf_logging.debug("expected = %s", expected)
        tf_logging.debug("actual = %s", value)
        if np.issubdtype(value.dtype, np.integer):
            self.assertAllEqual(np.rint(expected), np.ravel(value))
        else:
            self.assertAllCloseAccordingToType(
                expected, np.ravel(value), atol=tol, rtol=tol)
        self.assertShapeEqual(value, conv)
        self.assertEqual(value.dtype, conv.dtype.as_numpy_dtype)
