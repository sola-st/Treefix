# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(1,))
table.add_target(make_shape_function_type(1, 2))
table.add_target(make_shape_function_type(1, 2, 3))
self.assertEqual(
    list(table.targets), [
        make_shape_function_type(1,),
        make_shape_function_type(1, 2),
        make_shape_function_type(1, 2, 3)
    ])
