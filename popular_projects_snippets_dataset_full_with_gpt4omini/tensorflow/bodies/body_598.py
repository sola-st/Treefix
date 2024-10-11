# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_test.py
output_checker = tf_doctest_lib.TfDoctestOutputChecker()
self.assertTrue(
    output_checker.check_output(
        want=want, got=got, optionflags=doctest.ELLIPSIS))
