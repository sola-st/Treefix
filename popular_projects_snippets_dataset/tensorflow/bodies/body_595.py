# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_test.py
extract_floats = tf_doctest_lib._FloatExtractor()
output_checker = tf_doctest_lib.TfDoctestOutputChecker()

(text_parts, extracted_floats) = extract_floats(text)
text_with_wildcards = '...'.join(text_parts)

# Check that the lengths match before doing anything else.
try:
    self.assertLen(extracted_floats, len(expected_floats))
except AssertionError as e:
    msg = '\n\n  expected: {}\n  found:     {}'.format(
        expected_floats, extracted_floats)
    e.args = (e.args[0] + msg,)
    raise e

# The floats should match according to allclose
try:
    self.assertTrue(
        output_checker._allclose(expected_floats, extracted_floats))
except AssertionError as e:
    msg = '\n\nexpected:  {}\nfound:     {}'.format(expected_floats,
                                                    extracted_floats)
    e.args = (e.args[0] + msg,)
    raise e

# The wildcard text should match the input text, according to the
# OutputChecker base class.
try:
    self.assertTrue(doctest.OutputChecker().check_output(
        want=text_with_wildcards, got=text, optionflags=doctest.ELLIPSIS))
except AssertionError as e:
    msg = '\n\n  expected: {}\n  found:     {}'.format(
        text_with_wildcards, text)
    e.args = (e.args[0] + msg,)
    raise e
