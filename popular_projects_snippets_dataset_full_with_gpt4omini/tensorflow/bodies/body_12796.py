# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
counter = variable_scope.get_variable(
    "my_counter", shape=[], initializer=init_ops.zeros_initializer())
increment_counter = state_ops.assign_add(counter, 1)
const_with_dep = control_flow_ops.with_dependencies(
    (increment_counter, constant_op.constant(42)), constant_op.constant(7))

self.evaluate(variables.global_variables_initializer())
self.assertEqual(0, self.evaluate(counter))
self.assertEqual(7, self.evaluate(const_with_dep))
self.assertEqual(1, self.evaluate(counter))
