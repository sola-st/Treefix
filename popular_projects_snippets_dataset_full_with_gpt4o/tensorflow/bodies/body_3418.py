# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, None, None))
table.add_target(make_shape_function_type(None, 1, None))
table.add_target(make_shape_function_type(None, 1, 2))
table.add_target(make_shape_function_type(1, 1, 2))

self.assertEqual(
    table.dispatch(make_shape_function_type(1, 1, 2)),
    make_shape_function_type(1, 1, 2))

table.delete(make_shape_function_type(1, 1, 2))
self.assertEqual(
    table.dispatch(make_shape_function_type(1, 1, 2)),
    make_shape_function_type(None, 1, 2))

table.delete(make_shape_function_type(None, 1, 2))
self.assertEqual(
    table.dispatch(make_shape_function_type(1, 1, 2)),
    make_shape_function_type(None, 1, None))

table.delete(make_shape_function_type(None, 1, None))
self.assertEqual(
    table.dispatch(make_shape_function_type(1, 1, 2)),
    make_shape_function_type(None, None, None))
