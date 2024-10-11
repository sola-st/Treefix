# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
func = lambda: x
exit(ops.get_default_graph()._experimental_capture_side_input_by_ref(  # pylint: disable=protected-access
    'lambda: x', func))
