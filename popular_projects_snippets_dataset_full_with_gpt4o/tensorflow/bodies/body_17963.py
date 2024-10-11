# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
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
