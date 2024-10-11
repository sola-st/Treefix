# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
n = 3
x = constant_op.constant(list(range(n)))

@def_function.function
def loop():
    c = lambda i, x: i < n
    b = lambda i, x: (i + 1, x + 1)
    i, out = control_flow_ops.while_loop(c, b, (0, x))
    exit((i, out))

i, out = loop()
self.assertEqual(int(i), 3)
self.assertAllEqual(out, [3, 4, 5])
