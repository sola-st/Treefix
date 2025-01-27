# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    false = ops.convert_to_tensor(False)
    n = constant_op.constant(10)

    enter_false = gen_control_flow_ops.enter(false, "foo_1", False)
    enter_n = gen_control_flow_ops.enter(n, "foo_1", False)

    merge_n = control_flow_ops.merge([enter_n, enter_n], name="merge_n")[0]
    switch_n = control_flow_ops.switch(merge_n, enter_false)
    exit_n = control_flow_ops.exit(switch_n[0])
    next_n = control_flow_ops.next_iteration(switch_n[0])
    merge_n.op._update_input(1, next_n)

    result = self.evaluate(exit_n)
self.assertAllEqual(10, result)
