# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
with self.assertRaisesRegex(xla_client.XlaRuntimeError, "invalid shape"):
    xla_client.Shape.array_shape(xla_client.PrimitiveType.F32, [-2, 4])

with self.assertRaisesRegex(
    RuntimeError, "layout minor_to_major field contains 1 element.*"):
    xla_client.Shape.array_shape(xla_client.PrimitiveType.F32, [2, 4], [3])

with self.assertRaisesRegex(
    RuntimeError, "layout minor_to_major field has out-of-bounds value.*"):
    xla_client.Shape.array_shape(xla_client.PrimitiveType.F32, [2, 4],
                                 [1, -1])
