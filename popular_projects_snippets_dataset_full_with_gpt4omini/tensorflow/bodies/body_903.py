# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
"""Verifies against `Failed precondition: Expected one input shape`."""

with self.session(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    for pred in True, False:
        cond_out = control_flow_ops.cond(
            array_ops.placeholder_with_default(pred, []),
            lambda: constant_op.constant(2.),
            lambda: constant_op.constant(1.))
        self.assertEqual(int(pred) + 1., self.evaluate(cond_out))

    xla_context.Exit()
