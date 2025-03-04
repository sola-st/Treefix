# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
strides = [1, 1, 1, 1]
padding = "SAME"
if tin is None:
    tin = math_ops.cast(
        constant_op.constant(1, shape=[1, 2, 3, 3]), dtype=dtypes.quint8)

if tfilter is None:
    tfilter = math_ops.cast(
        constant_op.constant(1, shape=[1, 2, 3, 3]), dtype=dtypes.quint8)

if min_input is None:
    min_input = constant_op.constant(0, shape=[], dtype=dtypes.float32)

if max_input is None:
    max_input = constant_op.constant(0, shape=[], dtype=dtypes.float32)

if min_filter is None:
    min_filter = constant_op.constant(0, shape=[], dtype=dtypes.float32)

if max_filter is None:
    max_filter = constant_op.constant(0, shape=[], dtype=dtypes.float32)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            error_regex):
    self.evaluate(
        nn_ops.quantized_conv2d(
            tin,
            tfilter,
            out_type=dtypes.qint32,
            strides=strides,
            padding=padding,
            min_input=min_input,
            max_input=max_input,
            min_filter=min_filter,
            max_filter=max_filter))
