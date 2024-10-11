# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, None))
table.add_target(make_shape_function_type(None, 1))
table.add_target(make_shape_function_type(None, 2))

self.assertEqual(
    list(table.targets), [
        make_shape_function_type(None, None),
        make_shape_function_type(None, 1),
        make_shape_function_type(None, 2)
    ])

table.delete(make_shape_function_type(None, 2))  # Should remove the target

self.assertEqual(
    list(table.targets), [
        make_shape_function_type(None, None),
        make_shape_function_type(None, 1),
    ])

table.delete(make_shape_function_type(None, 2))  # Should have no effect

self.assertEqual(
    list(table.targets), [
        make_shape_function_type(None, None),
        make_shape_function_type(None, 1),
    ])
