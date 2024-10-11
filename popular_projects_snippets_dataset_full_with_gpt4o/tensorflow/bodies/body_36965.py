# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():

    def compute(i, m, c, o):
        m, c = [math_ops.add(m, 1), math_ops.add(c, 1)]
        o = math_ops.add(o, m)
        o = math_ops.add(o, c)
        i = math_ops.add(i, 1)
        exit([i, m, c, o])

    i = ops.convert_to_tensor(0)
    m = ops.convert_to_tensor(0)
    c = ops.convert_to_tensor(0)
    o = ops.convert_to_tensor(0)
    d = ops.convert_to_tensor(100)
    r = control_flow_ops.while_loop(lambda i, m, c, o: math_ops.less(i, d),
                                    compute, [i, m, c, o])
    result = r[3]
self.assertAllEqual(10100, result)
