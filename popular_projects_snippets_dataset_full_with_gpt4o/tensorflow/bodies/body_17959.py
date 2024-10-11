# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x1 = array_ops.gather(x, i)
exit(nn.conv2d(
    x1, filt, strides=[1, 2, 2, 1], padding="VALID", data_format="NHWC"))
