# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
a = ExtensionTypeTest.Node(5)
self.assertAllEqual(a.x, 5)
self.assertIsNone(a.y)
self.assertEqual(a.children, ())

b = ExtensionTypeTest.Node(6, 'blue')
self.assertAllEqual(b.x, 6)
self.assertEqual(b.y, 'blue')
self.assertEqual(b.children, ())

c = ExtensionTypeTest.Node(7, children=(a, b))
self.assertAllEqual(c.x, 7)
self.assertIsNone(c.y)
self.assertEqual(c.children, (a, b))
