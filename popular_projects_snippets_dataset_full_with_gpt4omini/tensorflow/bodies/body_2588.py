# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
a = xla_client.ShapeIndex((1, 2))
b = xla_client.ShapeIndex((1, 2))
c = xla_client.ShapeIndex((2, 3))
self.assertEqual(a, b)
self.assertNotEqual(b, c)
