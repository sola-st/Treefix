# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
input_nhwc = math_ops.cast(inputs, dtype)
with self.cached_session(use_gpu=False):
    # test NHWC (default) on CPU
    x_tf = array_ops.depth_to_space(input_nhwc, block_size)
    self.assertAllEqual(x_tf, outputs)

    # Run this test only if only CPU device is available
    if all(x.device_type == "CPU" for x in device_lib.list_local_devices()):
        input_nchw = test_util.NHWCToNCHW(input_nhwc)
        output_nchw = array_ops.depth_to_space(
            input_nchw, block_size, data_format="NCHW")
        output_nhwc = test_util.NCHWToNHWC(output_nchw)
        with self.assertRaisesRegex(
            errors_impl.InvalidArgumentError,
            "No OpKernel was registered to support Op 'DepthToSpace'"):
            self.evaluate(output_nhwc)

if test.is_gpu_available():
    with self.cached_session():
        # test NHWC (default) on GPU
        x_tf = array_ops.depth_to_space(input_nhwc, block_size)
        self.assertAllEqual(x_tf, outputs)
        # test NCHW on GPU
        input_nchw = test_util.NHWCToNCHW(input_nhwc)
        output_nchw = array_ops.depth_to_space(
            input_nchw, block_size, data_format="NCHW")
        output_nhwc = test_util.NCHWToNHWC(output_nchw)
        self.assertAllEqual(output_nhwc, outputs)
