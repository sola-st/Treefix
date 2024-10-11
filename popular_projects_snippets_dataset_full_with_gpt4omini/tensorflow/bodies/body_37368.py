# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with context.eager_mode():
    try:
        @def_function.function
        def set_step(step):
            summary_ops.set_step(step)
            exit(summary_ops.get_step())
        @def_function.function
        def get_and_increment():
            summary_ops.get_step().assign_add(1)
            exit(summary_ops.get_step())
        mystep = variables.Variable(0)
        self.assertAllEqual(0, set_step(mystep))
        self.assertAllEqual(0, summary_ops.get_step().read_value())
        self.assertAllEqual(1, get_and_increment())
        self.assertAllEqual(2, get_and_increment())
        # Check that set_step() properly maintains reference to variable.
        del mystep
        self.assertAllEqual(3, get_and_increment())
    finally:
        # Reset to default state for other tests.
        summary_ops.set_step(None)
