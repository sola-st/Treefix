# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
obj = NonLayerTrackable()
with self.assertRaisesRegex(ValueError, "do not specify shape"):
    trackable_utils.add_variable(
        obj, name="shape_specified_twice", shape=[], initializer=1)
constant_initializer = trackable_utils.add_variable(
    obj, name="constant_initializer", initializer=1)
with variable_scope.variable_scope("some_variable_scope"):
    ones_initializer = trackable_utils.add_variable(
        obj,
        name="ones_initializer",
        shape=[2],
        initializer=init_ops.ones_initializer(dtype=dtypes.float32))
bare_initializer = trackable_utils.add_variable(
    obj,
    name="bare_initializer",
    shape=[2, 2],
    dtype=dtypes.float64,
    initializer=init_ops.zeros_initializer)

# Even in graph mode, there are no naming conflicts between objects, only
# naming conflicts within an object.
other_duplicate = resource_variable_ops.ResourceVariable(
    name="duplicate", initial_value=1.)
duplicate = trackable_utils.add_variable(
    obj, name="duplicate", shape=[])
with self.assertRaisesRegex(ValueError, "'duplicate'.*already declared"):
    trackable_utils.add_variable(obj, name="duplicate", shape=[])

self.evaluate(trackable_utils.gather_initializers(obj))
self.assertEqual("constant_initializer:0", constant_initializer.name)
self.assertEqual(1, self.evaluate(constant_initializer))
self.assertEqual("some_variable_scope/ones_initializer:0",
                 ones_initializer.name)
self.assertAllEqual([1, 1], self.evaluate(ones_initializer))
self.assertAllEqual([[0., 0.],
                     [0., 0.]], self.evaluate(bare_initializer))
self.assertEqual("a_variable:0", obj.a_variable.name)
self.assertEqual("duplicate:0", other_duplicate.name)
if context.executing_eagerly():
    # When executing eagerly, there's no uniquification of variable names. The
    # checkpoint name will be the same.
    self.assertEqual("duplicate:0", duplicate.name)
else:
    # The .name attribute may be globally influenced, but the checkpoint name
    # won't be (tested below).
    self.assertEqual("duplicate_1:0", duplicate.name)

expected_checkpoint_names = {
    "a_variable/.ATTRIBUTES/VARIABLE_VALUE",
    "bare_initializer/.ATTRIBUTES/VARIABLE_VALUE",
    "constant_initializer/.ATTRIBUTES/VARIABLE_VALUE",
    "duplicate/.ATTRIBUTES/VARIABLE_VALUE",
    "ones_initializer/.ATTRIBUTES/VARIABLE_VALUE",
}
actual_checkpoint_names = _get_all_checkpoint_names(obj)
self.assertEqual(expected_checkpoint_names, set(actual_checkpoint_names))
