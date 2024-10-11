# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
integer_types = [
    dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64, dtypes.uint8,
    dtypes.uint16, dtypes.uint32, dtypes.uint64
]

# Floats are not compatible with ints
for t in integer_types:
    with self.assertRaises(TypeError):
        constant_op.constant(0.5, dtype=t)

    # Ints compatible with floats
self.assertEqual(
    self.evaluate(constant_op.constant(5, dtype=dtypes.float16)), 5.0)
self.assertEqual(
    self.evaluate(constant_op.constant(5, dtype=dtypes.float32)), 5.0)
self.assertEqual(
    self.evaluate(constant_op.constant(5, dtype=dtypes.float64)), 5.0)
self.assertEqual(
    self.evaluate(constant_op.constant(5, dtype=dtypes.bfloat16)), 5.0)

# Ints and floats are compatible with complex types
self.assertEqual(
    constant_op.constant([[1.0]], dtype=dtypes.complex128).dtype,
    dtypes.complex128)
self.assertEqual(
    constant_op.constant([[1]], dtype=dtypes.complex128).dtype,
    dtypes.complex128)

# Quantized types are not compatible with floats
quantized_types = [
    dtypes.qint16, dtypes.qint32, dtypes.qint8, dtypes.quint16,
    dtypes.quint8
]

for t in quantized_types:
    with self.assertRaises(TypeError):
        constant_op.constant(0.5, dtype=t)
