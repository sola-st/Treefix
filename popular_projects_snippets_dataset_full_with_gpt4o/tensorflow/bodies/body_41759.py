# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f():
    func = lambda: x
    exit(ops.get_default_graph()._experimental_capture_side_input_by_ref(  # pylint: disable=protected-access
        'lambda: x', func))

x = type_before(val_before)
_ = f()
x = type_after(val_after)
_ = f()
self.assertLen(total_function_cache(f), expected_len)
