# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    data = constant_op.constant([1, 2, 3, 4, 5, 6], name="data")
    ports = ops.convert_to_tensor(True, name="ports")
    switch_op = control_flow_ops.switch(data, ports)
    dead_branch = array_ops.identity(switch_op[0])

    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        lambda e: "Retval[0] does not have value" in str(e)):
        self.evaluate(dead_branch)
