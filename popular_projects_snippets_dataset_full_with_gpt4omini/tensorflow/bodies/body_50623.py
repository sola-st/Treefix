# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
for dtype in (dtypes.int8, dtypes.uint8, dtypes.int16, dtypes.int32,
              dtypes.float32, dtypes.float64):
    const = constant_op.constant(10, dtype=dtype)
    summary_lib.histogram('h', const)
