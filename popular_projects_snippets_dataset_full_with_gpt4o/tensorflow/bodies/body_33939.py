# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/quantization_ops/quantization_ops_test.py
x = constant_op.constant(
    np.int8(0), shape=[3, 3, 3, 3], dtype=dtypes.quint8)
y = constant_op.constant(np.int8(0), shape=[3], dtype=dtypes.quint8)

with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be rank 0"):
    self.evaluate(
        math_ops.quantized_add(
            x=x,
            y=y,
            min_x=[],
            max_x=1.0,
            min_y=0.0,
            max_y=1.0,
            Toutput=dtypes.qint32))
