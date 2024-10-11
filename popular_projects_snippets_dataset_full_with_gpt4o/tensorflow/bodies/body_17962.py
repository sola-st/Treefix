# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
self.skipTest("b/262851489: Fix nightly build for GPU.")
x_shape = [2, 12, 12, 3]
filt = random_ops.random_uniform([3, 3, 3, 7])
grad = random_ops.random_uniform([3, 2, 5, 5, 7])

def loop_fn(i):
    grad1 = array_ops.gather(grad, i)
    exit(nn.conv2d_backprop_input(
        x_shape,
        filt,
        grad1,
        strides=[1, 2, 2, 1],
        padding="VALID",
        data_format="NHWC"))

self._test_loop_fn(loop_fn, 3)
