# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Checks that datasets raise the same error on the first get_next call."""
if replacements is None:
    replacements = []
next1 = self.getNext(dataset1)
next2 = self.getNext(dataset2)
try:
    self.evaluate(next1())
    raise ValueError(
        "Expected dataset to raise an error of type %s, but it did not." %
        repr(exception_class))
except exception_class as e:
    expected_message = e.message
    for old, new, count in replacements:
        expected_message = expected_message.replace(old, new, count)
    # Check that the first segment of the error messages are the same.
    with self.assertRaisesRegexp(exception_class,
                                 re.escape(expected_message)):
        self.evaluate(next2())
