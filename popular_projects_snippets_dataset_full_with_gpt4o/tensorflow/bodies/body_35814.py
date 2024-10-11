# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
constraint = lambda x: x
v = variables.Variable(
    lambda: constant_op.constant(1.),
    constraint=constraint)
self.assertEqual(v.constraint, constraint)

constraint = 0
with self.assertRaises(ValueError):
    v = variables.Variable(
        lambda: constant_op.constant(1.),
        constraint=constraint)
