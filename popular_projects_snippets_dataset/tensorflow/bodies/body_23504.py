# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_test.py
root = base.Trackable()
a = root._add_variable_with_custom_getter(
    name="v", shape=[], getter=variable_scope.get_variable)
self.assertEqual([root, a], util.list_objects(root))
with ops.Graph().as_default():
    b = root._add_variable_with_custom_getter(
        name="v", shape=[], overwrite=True,
        getter=variable_scope.get_variable)
    self.assertEqual([root, b], util.list_objects(root))
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError,
                                "already declared as a dependency"):
        root._add_variable_with_custom_getter(
            name="v", shape=[], overwrite=False,
            getter=variable_scope.get_variable)
