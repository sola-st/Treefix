# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    zero = constant_op.constant(0)
    one = constant_op.constant(1)
    n = constant_op.constant(10)

    enter_i = gen_control_flow_ops.enter(zero, "foo", False)
    enter_one = gen_control_flow_ops.enter(one, "foo", True)
    enter_n = gen_control_flow_ops.enter(n, "foo", True)

    with ops.device(test.gpu_device_name()):
        merge_i = control_flow_ops.merge([enter_i, enter_i])[0]

    less_op = math_ops.less(merge_i, enter_n)
    cond_op = control_flow_ops.loop_cond(less_op)
    switch_i = control_flow_ops.switch(merge_i, cond_op)

    add_i = math_ops.add(switch_i[1], enter_one)

    next_i = control_flow_ops.next_iteration(add_i)
    merge_i.op._update_input(1, next_i)

    exit_i = control_flow_ops.exit(switch_i[0])
    result = self.evaluate(exit_i)
self.assertAllEqual(10, result)
