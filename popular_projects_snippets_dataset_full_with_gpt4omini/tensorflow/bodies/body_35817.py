# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    v_def = variables.Variable(
        initial_value=constant_op.constant(3.0)).to_proto()

with ops.Graph().as_default(), self.cached_session() as sess:
    # v describes a VariableDef-based variable without an initial value.
    v = variables.Variable(variable_def=v_def)
    self.assertEqual(3.0, self.evaluate(v.initialized_value()))

    # initialized_value should not rerun the initializer_op if the variable
    # has already been initialized elsewhere.
    self.evaluate(v.assign(1.0))
    self.assertEqual(1.0, self.evaluate(v.initialized_value()))

v_def.ClearField("initial_value_name")
with ops.Graph().as_default(), self.cached_session() as sess:
    # Restoring a legacy VariableDef proto that does not have
    # initial_value_name set should still work.
    v = variables.Variable(variable_def=v_def)
    # We should also be able to re-export the variable to a new meta graph.
    self.assertProtoEquals(v_def, v.to_proto())
    # But attempts to use initialized_value will result in errors.
    with self.assertRaises(ValueError):
        self.evaluate(v.initialized_value())
