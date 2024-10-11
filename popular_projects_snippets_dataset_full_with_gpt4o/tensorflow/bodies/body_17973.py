# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
grad1 = array_ops.gather(grad, i)
filt1 = array_ops.gather(filt, i)
exit(nn.depthwise_conv2d_native_backprop_input(
    x_shape,
    filt1,
    grad1,
    strides=[1, 1, 2, 2],
    padding="VALID",
    data_format="NCHW"))
