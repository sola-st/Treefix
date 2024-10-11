# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
table = type_dispatch.TypeDispatchTable()
table.add_target(make_shape_function_type(None, None, None))
table.add_target(make_shape_function_type(None, 1))
table.add_target(make_shape_function_type(1, 1))
table.add_target(make_shape_function_type(None, 2, 1))

self.assertIn(make_shape_function_type(None, None, None), table.targets)
self.assertIn(make_shape_function_type(None, 1), table.targets)
self.assertIn(make_shape_function_type(1, 1), table.targets)
self.assertIn(make_shape_function_type(None, 2, 1), table.targets)

self.assertNotIn(make_shape_function_type(None, None, 1), table.targets)
self.assertNotIn(make_shape_function_type(1, None), table.targets)
self.assertNotIn(make_shape_function_type(1, 2), table.targets)
self.assertNotIn(make_shape_function_type(None, 2, None), table.targets)
