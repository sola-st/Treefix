# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
self._testBadInputSize(
    tin=math_ops.cast(
        constant_op.constant(1, shape=[1, 2]), dtype=dtypes.quint8),
    error_regex="must be rank 4")
self._testBadInputSize(
    tfilter=math_ops.cast(
        constant_op.constant(1, shape=[1, 2]), dtype=dtypes.quint8),
    error_regex="must be rank 4")
self._testBadInputSize(
    min_input=constant_op.constant(0, shape=[1], dtype=dtypes.float32),
    error_regex="must be rank 0")
self._testBadInputSize(
    max_input=constant_op.constant(0, shape=[1], dtype=dtypes.float32),
    error_regex="must be rank 0")
self._testBadInputSize(
    min_filter=constant_op.constant(0, shape=[1], dtype=dtypes.float32),
    error_regex="must be rank 0")
self._testBadInputSize(
    max_filter=constant_op.constant(0, shape=[1], dtype=dtypes.float32),
    error_regex="must be rank 0")
