# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/simple_save_test.py
self.assertEqual(actual_variable.name, expected_variable.name)
self.assertEqual(actual_variable.dtype, expected_variable.dtype)
self.assertEqual(len(actual_variable.shape), len(expected_variable.shape))
for i in range(len(actual_variable.shape)):
    self.assertEqual(actual_variable.shape[i], expected_variable.shape[i])
