# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_test.py
extract_floats = tf_doctest_lib._FloatExtractor()
output_checker = tf_doctest_lib.TfDoctestOutputChecker()

(_, extracted_floats) = extract_floats(text)

# These floats should not match according to allclose
try:
    self.assertFalse(
        output_checker._allclose(expected_floats, extracted_floats))
except AssertionError as e:
    msg = ('\n\nThese matched! They should not have.\n'
           '\n\n  Expected:  {}\n  found:     {}'.format(
               expected_floats, extracted_floats))
    e.args = (e.args[0] + msg,)
    raise e
