# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

class NoABCControlFlowContext(control_flow_ops.ControlFlowContext):
    """A noop wrapper around `ControlFlowContext`.

      `ControlFlowContext` is an ABC and therefore cannot be instantiated.
      """

    # pylint: disable=useless-super-delegation

    def to_control_flow_context_def(self, context_def, export_scope=None):
        super(NoABCControlFlowContext,
              self).to_control_flow_context_def(context_def, export_scope)

with self.cached_session():
    constant_op.constant(0, name="a")
    constant_op.constant(2, name="test_scope/a")
    b1 = constant_op.constant(1, name="b")
    b2 = constant_op.constant(3, name="test_scope/b")

    c = NoABCControlFlowContext()
    c._values = ["a", "b"]
    c._external_values = {"a": b1}

    c_with_scope = NoABCControlFlowContext(
        values_def=c._to_values_def(), import_scope="test_scope")

    # _values and _external_values should be have scope prepended.
    self.assertEqual(c_with_scope._values,
                     set(["test_scope/a", "test_scope/b"]))
    self.assertEqual(c_with_scope._external_values, {"test_scope/a": b2})

    # Calling _to_proto() with export_scope should remove "test_scope".
    self.assertProtoEquals(
        c._to_values_def(),
        c_with_scope._to_values_def(export_scope="test_scope"))
