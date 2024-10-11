# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

mytuple = deprecation.deprecated(
    date, instructions, warn_once=True)(
        collections.namedtuple("my_tuple", ["field1", "field2"]))

mytuple(1, 2)
self.assertEqual(1, mock_warning.call_count)
mytuple(3, 4)
self.assertEqual(1, mock_warning.call_count)
self.assertIn("IS DEPRECATED", mytuple.__doc__)
