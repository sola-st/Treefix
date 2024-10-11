# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
input_nhwc = math_ops.cast(inputs, dtype)
# test NHWC (default)
x_tf = array_ops.space_to_depth(input_nhwc, block_size)
self.assertAllEqual(self.evaluate(x_tf), outputs)

if test_util.is_gpu_available():
    with test_util.force_gpu():
        # test NCHW on GPU
        input_nchw = test_util.NHWCToNCHW(input_nhwc)
        output_nchw = array_ops.space_to_depth(
            input_nchw, block_size, data_format="NCHW")
        output_nhwc = test_util.NCHWToNHWC(output_nchw)
        self.assertAllEqual(self.evaluate(output_nhwc), outputs)
