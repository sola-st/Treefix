# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
class MyClass(object):
    """My docstring."""

    init_args = []

    def __init__(self, arg):
        MyClass.init_args.append(arg)

deprecated_cls = deprecation.deprecated_alias("deprecated.cls",
                                              "real.cls",
                                              MyClass)

print(deprecated_cls.__name__)
print(deprecated_cls.__module__)
print(deprecated_cls.__doc__)

MyClass("test")
self.assertEqual(0, mock_warning.call_count)
deprecated_cls("deprecated")
self.assertEqual(1, mock_warning.call_count)
# Make sure the error points to the right file.
self.assertRegex(mock_warning.call_args[0][1], r"deprecation_test\.py:")
deprecated_cls("deprecated again")
self.assertEqual(1, mock_warning.call_count)

self.assertEqual(["test", "deprecated", "deprecated again"],
                 MyClass.init_args)

# Check __init__ signature matches for doc generation.
self.assertEqual(
    tf_inspect.getfullargspec(MyClass.__init__),
    tf_inspect.getfullargspec(deprecated_cls.__init__))
