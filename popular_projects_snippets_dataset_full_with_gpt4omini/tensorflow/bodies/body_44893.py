# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
with self.assertRaisesRegex(ValueError, 'unknown type'):
    special_functions.tensor_list(np.array([1, 2, 3]))
