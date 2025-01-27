# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, 1, None))
table.add_target(make_shape_function_type(None, 1, 2))
table.add_target(make_shape_function_type(None, 2, 2))

self.assertIsNone(table.dispatch(make_shape_function_type(1, 2)))
self.assertIsNone(table.dispatch(make_shape_function_type(1, 2, 3)))
self.assertIsNone(table.dispatch(make_shape_function_type(1, 2, 3, 4)))
