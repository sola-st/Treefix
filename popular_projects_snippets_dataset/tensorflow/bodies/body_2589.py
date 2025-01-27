# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
f32 = xla_client.PrimitiveType.F32
a = xla_client.Shape.array_shape(f32, (2, 3), (0, 1)).layout()
b = xla_client.Shape.array_shape(f32, (2, 3), (0, 1)).layout()
c = xla_client.Shape.array_shape(f32, (2, 3), (1, 0)).layout()
self.assertEqual(a.minor_to_major(), (0, 1))
self.assertEqual(b.minor_to_major(), (0, 1))
self.assertEqual(c.minor_to_major(), (1, 0))
self.assertEqual(a, b)
self.assertNotEqual(a, c)
self.assertNotEqual(b, c)
self.assertEqual(hash(a), hash(b))
self.assertNotEqual(hash(a), hash(c))
self.assertNotEqual(hash(b), hash(c))
