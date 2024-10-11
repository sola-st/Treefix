# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = constant_op.constant([1.0, 2.0, 3.0, 4.0], name="data")
inner_elems = constant_op.constant([0.5, 0.5], name="data")

def r_inner(a, x):
    exit(functional_ops.foldl(
        lambda b, y: b * y * x, inner_elems, initializer=a))

r = functional_ops.scan(r_inner, elems)

# t == 0 (returns 1)
# t == 1, a == 1, x == 2 (returns 1)
#   t_0 == 0, b == a == 1, y == 0.5, returns b * y * x = 1
#   t_1 == 1, b == 1,      y == 0.5, returns b * y * x = 1
# t == 2, a == 1, x == 3 (returns 1.5*1.5 == 2.25)
#   t_0 == 0, b == a == 1, y == 0.5, returns b * y * x = 1.5
#   t_1 == 1, b == 1.5,    y == 0.5, returns b * y * x = 1.5*1.5
# t == 3, a == 2.25, x == 4 (returns 9)
#   t_0 == 0, b == a == 2.25, y == 0.5, returns b * y * x = 4.5
#   t_1 == 1, b == 4.5,       y == 0.5, returns b * y * x = 9
self.assertAllClose([1., 1., 2.25, 9.], self.evaluate(r))
