# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, 1, None))
table.add_target(make_shape_function_type(None, 1, 2))
self.assertEqual(
    table.try_generalizing_function_type(
        make_shape_function_type(None, 2, 3)),
    make_shape_function_type(None, None, None))
