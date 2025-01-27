# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
with self.assertRaisesRegex(ValueError,
                            'element_dtype and element_shape are required'):
    special_functions.tensor_list([])
