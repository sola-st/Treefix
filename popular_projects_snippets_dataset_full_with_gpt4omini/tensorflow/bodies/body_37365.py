# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with context.eager_mode():
    try:
        mystep = variables.Variable(0)
        summary_ops.set_step(mystep)
        self.assertAllEqual(0, summary_ops.get_step().read_value())
        mystep.assign_add(1)
        self.assertAllEqual(1, summary_ops.get_step().read_value())
        # Check that set_step() properly maintains reference to variable.
        del mystep
        self.assertAllEqual(1, summary_ops.get_step().read_value())
        summary_ops.get_step().assign_add(1)
        self.assertAllEqual(2, summary_ops.get_step().read_value())
    finally:
        # Reset to default state for other tests.
        summary_ops.set_step(None)
