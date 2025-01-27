# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
test_obj = structure.NoneTensorSpec()
with self.assertRaisesRegex(
    ValueError, r"No `TypeSpec` is compatible with both NoneTensorSpec\(\) "
    "and 100"):
    test_obj.most_specific_compatible_shape(100)
self.assertEqual(test_obj,
                 test_obj.most_specific_compatible_shape(test_obj))
