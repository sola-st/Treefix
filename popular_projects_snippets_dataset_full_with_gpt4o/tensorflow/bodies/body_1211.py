# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
for dtype in self.numeric_types:
    init = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8j, 9, 10,
                                                  11]]).astype(dtype)
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable(init)
        sess.run(variables.variables_initializer([v]))
        x = v.sparse_read(2)
        self.assertAllClose(
            np.array([8j, 9, 10, 11]).astype(dtype), self.evaluate(x))
