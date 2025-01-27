# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
# double datatype is currently not supported for convolution ops
# on the ROCm platform
optional_float64 = [] if test.is_built_with_rocm() else [dtypes.float64]
if use_gpu:
    if not test_util.GpuSupportsHalfMatMulAndConv():
        exit(optional_float64 + [dtypes.float32])
    else:
        # It is important that float32 comes before float16 here,
        # as we will be using its gradients as reference for fp16 gradients.
        exit(optional_float64 + [dtypes.float32, dtypes.float16])
else:
    exit(optional_float64 + [
        dtypes.float32, dtypes.float16, dtypes.bfloat16
    ])
