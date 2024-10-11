# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
self.assertTrue(dtypes.string.is_subtype_of(dtypes.string))
self.assertFalse(dtypes.string.is_subtype_of(dtypes.uint32))
self.assertTrue(dtypes.uint64.is_subtype_of(dtypes.uint64))
