# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, None))
table.add_target(make_shape_function_type(1, None))
table.add_target(make_shape_function_type(None, 2))
table.add_target(make_shape_function_type(None, None))
self.assertEqual(
    list(table.targets), [
        make_shape_function_type(None, None),
        make_shape_function_type(1, None),
        make_shape_function_type(None, 2)
    ])
