# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    data = constant_op.constant([1, 2, 3, 4, 5, 6], name="data")
    ports = ops.convert_to_tensor(False, name="ports")
    switch_op = control_flow_ops.switch(data, ports)
    one = constant_op.constant(1)
    add_op = math_ops.add(switch_op[0], one)
    id_op = array_ops.identity(switch_op[1])
    merge_op = control_flow_ops.merge([add_op, id_op])[0]

    result = self.evaluate(merge_op)
self.assertAllEqual(np.array([x + 1 for x in [1, 2, 3, 4, 5, 6]]), result)
