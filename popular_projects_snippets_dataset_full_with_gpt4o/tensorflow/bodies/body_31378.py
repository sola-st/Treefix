# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if test_util.IsMklEnabled():
    exit([dtypes.float32])

if use_gpu:
    # It is important that float32 comes first, since we are using its
    # gradients as a reference for fp16 gradients.
    out = [dtypes.float32]
    if test_util.GpuSupportsHalfMatMulAndConv():
        out.append(dtypes.float16)
    if not test.is_built_with_rocm():
        out.extend([dtypes.float64, dtypes.bfloat16])
    exit(out)

exit([dtypes.float32, dtypes.float64, dtypes.float16, dtypes.bfloat16])
