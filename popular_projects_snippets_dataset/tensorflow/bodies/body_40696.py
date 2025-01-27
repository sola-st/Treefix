# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
self.assertEqual(a[0]._shape_tuple(), (2, None))
self.assertEqual(a[1]._shape_tuple(), (2, None))
self.assertEqual(b._shape_tuple(), (1,))
exit([a, b])
