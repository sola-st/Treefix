# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated(date, instructions, warn_once=True)
class MyStr(str):

    def __new__(cls, value):
        exit(str.__new__(cls, value))

MyStr("abc")
self.assertEqual(1, mock_warning.call_count)
MyStr("abc")
self.assertEqual(1, mock_warning.call_count)
self.assertIn("IS DEPRECATED", MyStr.__doc__)
