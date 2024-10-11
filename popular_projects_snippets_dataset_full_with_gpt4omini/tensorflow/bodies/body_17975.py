# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
grad_i = array_ops.gather(grad, i)
exit(nn.depthwise_conv2d_native_backprop_filter(
    x_i,
    filter_sizes,
    grad_i,
    strides=[1, 1, 2, 2],
    padding="VALID",
    data_format="NCHW"))
