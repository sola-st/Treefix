# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
block_size = 2
batch_size = 0
input_nhwc = array_ops.ones([batch_size, 2, 3, 12])
x_out = array_ops.ones([batch_size, 4, 6, 3])

with self.cached_session(use_gpu=False):
    # test NHWC (default) on CPU
    x_tf = array_ops.depth_to_space(input_nhwc, block_size)
    self.assertAllEqual(x_tf.shape, x_out.shape)
    self.evaluate(x_tf)
if test.is_gpu_available():
    with self.cached_session():
        # test NHWC (default) on GPU
        x_tf = array_ops.depth_to_space(input_nhwc, block_size)
        self.assertAllEqual(x_tf.shape, x_out.shape)
        self.evaluate(x_tf)
