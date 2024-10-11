# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, 1))
table.add_target(make_shape_function_type(None, 2))
table.add_target(make_shape_function_type(None, 3))
self.assertEqual(
    table.try_generalizing_function_type(
        make_shape_function_type(None, 4, 3)),
    make_shape_function_type(None, 4, 3))
