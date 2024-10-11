# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.assertRaisesRegexp(
    ValueError, "NCHW_VECT_C.*is not supported with "
    "explicit padding|XLA does not support pooling ops with explicit "
    "padding"):
    nn_ops.max_pool(
        array_ops.placeholder(dtypes.float32, shape=[1, 3, 3, 1]),
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding=[[0, 0], [0, 1], [0, 1], [0, 0]],
        data_format="NCHW_VECT_C")
with self.assertRaisesRegexp(
    ValueError, "Explicit padding is not supported with an input "
                "tensor of rank 5"):
    nn_ops.max_pool_v2(
        array_ops.placeholder(dtypes.float32, shape=[1, 3, 3, 1, 1]),
        ksize=[1, 2, 2, 1, 1],
        strides=[1, 2, 2, 1, 1],
        padding=[[0, 0], [0, 1], [0, 1], [0, 0]],
        data_format="NCHW")
with self.assertRaisesRegexp(
    ValueError, "Attr 'padding' of 'MaxPoolV2' Op passed "
                "string 'EXPLICIT'"):
    gen_nn_ops.max_pool_v2(
        array_ops.placeholder(dtypes.float32, shape=[1, 3, 3, 1, 1]),
        ksize=[1, 2, 2, 1, 1],
        strides=[1, 2, 2, 1, 1],
        padding="EXPLICIT",
        data_format="NHWC")
