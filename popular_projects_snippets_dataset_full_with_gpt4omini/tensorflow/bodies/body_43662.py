# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated(date, instructions, warn_once=True)
class MyClass():
    """A test class."""

    def __init__(self, a):
        pass

MyClass("")
self.assertEqual(1, mock_warning.call_count)
MyClass("")
self.assertEqual(1, mock_warning.call_count)
self.assertIn("IS DEPRECATED", MyClass.__doc__)
