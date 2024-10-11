# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
# Regression test for a bug where computations with one non-constant
# output and one variable update were mishandled.
for dtype in self.numeric_types:
    init = np.array([[1, 2j], [3, 4]]).astype(dtype)
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable(init)
        sess.run(variables.variables_initializer([v]))
        p = array_ops.placeholder(dtype)
        x = v.assign_add(p)
        with ops.control_dependencies([x]):
            y = v.read_value()
        self.assertAllClose(
            np.array([[2, 1 + 2j], [4, 5]]).astype(dtype),
            sess.run(y, {p: [[1, 1], [1, 1]]}))
