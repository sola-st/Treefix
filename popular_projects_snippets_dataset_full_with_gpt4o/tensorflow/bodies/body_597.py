# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_test.py
want = 'text ... text'
got = 'text 1.0 1.2 1.9 text'
output_checker = tf_doctest_lib.TfDoctestOutputChecker()
self.assertTrue(
    output_checker.check_output(
        want=want, got=got, optionflags=doctest.ELLIPSIS))
