# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, None, None))
table.add_target(make_shape_function_type(None, None, 1))
table.add_target(make_shape_function_type(None, 1, 1))
table.add_target(make_shape_function_type(1, 1, 1))
self.assertEqual(
    list(table.targets), [
        make_shape_function_type(None, None, None),
        make_shape_function_type(None, None, 1),
        make_shape_function_type(None, 1, 1),
        make_shape_function_type(1, 1, 1)
    ])
