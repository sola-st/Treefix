# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
self.assertEqual(dtypes.string,
                 dtypes.string.most_specific_common_supertype([]))
self.assertEqual(
    dtypes.string,
    dtypes.string.most_specific_common_supertype([dtypes.string]))
self.assertIsNone(
    dtypes.string.most_specific_common_supertype([dtypes.uint32]))
