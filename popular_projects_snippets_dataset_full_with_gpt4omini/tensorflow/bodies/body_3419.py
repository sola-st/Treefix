# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table_1 = type_dispatch.TypeDispatchTable()
table_1.add_target(make_shape_function_type(1, None, None))
table_1.add_target(make_shape_function_type(None, 2, None))
table_1.add_target(make_shape_function_type(None, None, 3))

table_2 = type_dispatch.TypeDispatchTable()
table_2.add_target(make_shape_function_type(None, 2, None))
table_2.add_target(make_shape_function_type(1, None, None))
table_2.add_target(make_shape_function_type(None, None, 3))

table_3 = type_dispatch.TypeDispatchTable()
table_3.add_target(make_shape_function_type(None, None, 3))
table_3.add_target(make_shape_function_type(1, None, None))
table_3.add_target(make_shape_function_type(None, 2, None))

# table_1, table_2, table_3 have the same targets
self.assertEqual(set(table_1.targets), set(table_2.targets))
self.assertEqual(set(table_2.targets), set(table_3.targets))

# But they dispatch to the first target they find which does not have any
# more specific viable target.
shape = make_shape_function_type(1, 2, 3)
self.assertEqual(
    table_1.dispatch(shape), make_shape_function_type(1, None, None))
self.assertEqual(
    table_2.dispatch(shape), make_shape_function_type(None, 2, None))
self.assertEqual(
    table_3.dispatch(shape), make_shape_function_type(None, None, 3))
