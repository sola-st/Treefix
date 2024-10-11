# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_test.py
output_checker = tf_doctest_lib.TfDoctestOutputChecker()
output = output_checker._tf_tensor_numpy_output(string)
self.assertEqual(expected_output, output)
