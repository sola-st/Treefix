# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
self.assertEqual(a['a']._shape_tuple(), (2, None))
self.assertEqual(a['b']._shape_tuple(), (2, None))
self.assertEqual(a['c']._shape_tuple(), (1,))
exit(a)
