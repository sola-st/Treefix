# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.session():
    with ops.device("/cpu:0"):
        v = variables.Variable(7.0)

    x = constant_op.constant(10.0)
    pred = math_ops.less(1.0, 2.0)
    fn1 = lambda: math_ops.add(v, 1.0)
    fn2 = lambda: math_ops.subtract(x, 1.0)
    r = control_flow_ops.cond(pred, fn1, fn2)

    for op in x.graph.get_operations():
        if op.name == "cond/Add/Switch":
            self.assertDeviceEqual(op.device, "/cpu:0")
