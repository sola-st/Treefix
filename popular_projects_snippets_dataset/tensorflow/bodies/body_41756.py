# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
func = lambda: x
# TODO(b/263520817): Remove access to private attribute.
exit(ops.get_default_graph(
    )._function_captures._create_capture_placeholder(func))
