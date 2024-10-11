# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if not test_util.is_gpu_available():
    self.skipTest("NCHW only works on GPU")
x = random_ops.random_uniform([3, 2, 3, 12, 12])
filter_sizes = [3, 3, 3, 2]
grad = random_ops.random_uniform([3, 2, 6, 5, 5])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    grad_i = array_ops.gather(grad, i)
    exit(nn.depthwise_conv2d_native_backprop_filter(
        x_i,
        filter_sizes,
        grad_i,
        strides=[1, 1, 2, 2],
        padding="VALID",
        data_format="NCHW"))

self._test_loop_fn(loop_fn, 3)
