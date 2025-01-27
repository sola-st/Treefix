# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x1 = array_ops.gather(x, i)
filt1 = array_ops.gather(filt, i)
exit(nn.depthwise_conv2d_native(
    x1, filt1, strides=[1, 2, 2, 1], padding="VALID", data_format="NHWC"))
