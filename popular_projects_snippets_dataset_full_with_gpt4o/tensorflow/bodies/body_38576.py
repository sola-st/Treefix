# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/aggregate_ops_test.py
if test.is_gpu_available():
    exit([
        dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64,
        dtypes.complex64, dtypes.complex128, dtypes.int64
    ])
exit([dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,
        dtypes.float16, dtypes.float32, dtypes.float64, dtypes.complex64,
        dtypes.complex128])
