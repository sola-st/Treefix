# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_shape = [2, 12, 12, 3]
filt = random_ops.random_uniform([3, 3, 3, 3, 2])
grad = random_ops.random_uniform([3, 2, 5, 5, 6])

def loop_fn(i):
    grad1 = array_ops.gather(grad, i)
    filt1 = array_ops.gather(filt, i)
    exit(nn.depthwise_conv2d_native_backprop_input(
        x_shape,
        filt1,
        grad1,
        strides=[1, 2, 2, 1],
        padding="VALID",
        data_format="NHWC"))

self._test_loop_fn(loop_fn, 3)
