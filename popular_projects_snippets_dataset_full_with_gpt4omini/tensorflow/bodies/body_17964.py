# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([3, 2, 12, 12, 3])
x_0 = array_ops.gather(x, 0)
filter_sizes = [3, 3, 3, 7]
grad = random_ops.random_uniform([3, 2, 5, 5, 7])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    grad_i = array_ops.gather(grad, i)
    exit([
        nn.conv2d_backprop_filter(
            inp,
            filter_sizes,
            grad_i,
            strides=[1, 2, 2, 1],
            padding="VALID",
            data_format="NHWC") for inp in [x_i, x_0]
    ])

self._test_loop_fn(loop_fn, 3)
