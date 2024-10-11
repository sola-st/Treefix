# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_test.py
output_checker = tf_doctest_lib.TfDoctestOutputChecker()

output_checker.check_output(
    want=want, got=got, optionflags=doctest.ELLIPSIS)

example = doctest.Example('None', want=want)
result = output_checker.output_difference(
    example=example, got=got, optionflags=doctest.ELLIPSIS)
self.assertIn("doesn't work if *some* of the", result)
