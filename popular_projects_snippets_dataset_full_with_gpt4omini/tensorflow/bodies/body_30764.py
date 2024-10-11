# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
"""Try to create the mkl concat operation

    when one of the input's memory descriptor is in blocked format
    """
if test_util.IsMklEnabled():
    s0 = np.ones((1, 8188, 4092, 1), dtype=np.uint8).astype(np.float32)
    s1 = array_ops.strided_slice(
        s0, [0, 1, 1, 0], [0, -1, -1, 0], [1, 1, 1, 1],
        begin_mask=9,
        end_mask=9)
    s2 = array_ops.slice(s1, [0, 0, 0, 0], [-1, -1, -1, 1])
    s3_1 = array_ops.slice(s2, [0, 4, 4, 0], [-1, 8178, 4082, 1])
    s3_2 = array_ops.slice(s2, [0, 4, 4, 0], [-1, 8178, 4082, 1])
    filter4_1 = constant_op.constant([[[[1.18, -0.51]]]])
    s4_1 = nn_ops.conv2d(
        s3_1, filter4_1, strides=[1, 1, 1, 1], padding="VALID")
    filter4_2 = constant_op.constant([[[[1.38, -0.11]]]])
    s4_2 = nn_ops.conv2d(
        s3_2, filter4_2, strides=[1, 1, 1, 1], padding="VALID")
    s5_1 = array_ops.slice(s4_1, [0, 6, 6, 0], [-1, 1, 1, -1])
    s5_2 = array_ops.slice(s4_2, [0, 6, 6, 0], [-1, 1, 1, -1])
    x_concat = array_ops.concat([s5_1, s5_2], 3)
    self.evaluate(
        x_concat
    )  # This test is only meant to check the creation is not crashed
