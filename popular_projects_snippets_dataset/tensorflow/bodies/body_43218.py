# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
dispatch.update_docstrings_with_api_lists()
self.assertRegex(
    dispatch.dispatch_for_api.__doc__,
    r"(?s)  The TensorFlow APIs that may be overridden "
    r"by `@dispatch_for_api` are:\n\n.*"
    r"  \* `tf\.concat\(values, axis, name\)`\n.*"
    r"  \* `tf\.math\.add\(x, y, name\)`\n.*")
self.assertRegex(
    dispatch.dispatch_for_unary_elementwise_apis.__doc__,
    r"(?s)  The unary elementwise APIs are:\n\n.*"
    r"  \* `tf\.math\.abs\(x, name\)`\n.*"
    r"  \* `tf\.math\.cos\(x, name\)`\n.*")
self.assertRegex(
    dispatch.dispatch_for_binary_elementwise_apis.__doc__,
    r"(?s)  The binary elementwise APIs are:\n\n.*"
    r"  \* `tf\.math\.add\(x, y, name\)`\n.*"
    r"  \* `tf\.math\.multiply\(x, y, name\)`\n.*")
