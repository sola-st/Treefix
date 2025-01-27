# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    cyclic = control_flow_ops.while_loop(
        cond=lambda i: i < 10,
        body=lambda i: i + 1,
        loop_vars=(constant_op.constant(0),))
    initial_value = variables._try_guard_against_uninitialized_dependencies(
        "test", cyclic)
    self.assertIs(initial_value, cyclic)
