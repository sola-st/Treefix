# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
# GitHub issue 22110.
if not test.is_gpu_available():
    exit()
with self.session():
    x = array_ops.placeholder(dtypes.float32)
    f = np.ones([1, 1, 1, 1], np.float32)
    v = nn_impl.depthwise_conv2d(
        x, f, [1, 1, 1, 1], "VALID", rate=[2, 1], data_format="NCHW")
    self.assertAllEqual(
        np.ones([1, 1, 1, 1], np.float32),
        v.eval(feed_dict={x: np.ones([1, 1, 1, 1], np.float32)}))
