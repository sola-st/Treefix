# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated(date, instructions, warn_once=True)
class MyEnum(enum.Enum):
    a = 1
    b = 2

self.assertIs(MyEnum(1), MyEnum.a)
self.assertEqual(1, mock_warning.call_count)
self.assertIs(MyEnum(2), MyEnum.b)
self.assertEqual(1, mock_warning.call_count)
self.assertIn("IS DEPRECATED", MyEnum.__doc__)
