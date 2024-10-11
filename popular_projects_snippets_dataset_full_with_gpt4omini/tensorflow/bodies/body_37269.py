# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.device("/gpu:0"):
    # Always put loop body on GPU.
    nx = nn_ops.conv2d(
        input=x,
        filter=kernel,
        strides=[1, 1, 1, 1],
        padding="SAME",
        data_format="NHWC",
        name="conv2d")
    ni = math_ops.add(i, 1)
    exit((ni, nx))
