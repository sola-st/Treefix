# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
self.assertEqual(rt.values.shape.as_list(), [None])
self.assertEqual(rt.row_splits.shape.as_list(), [4])
exit(rt)
