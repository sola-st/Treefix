# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
grad1 = array_ops.gather(grad, i)
exit(nn.conv2d_backprop_input(
    x_shape,
    filt,
    grad1,
    strides=[1, 2, 2, 1],
    padding="VALID",
    data_format="NHWC"))
