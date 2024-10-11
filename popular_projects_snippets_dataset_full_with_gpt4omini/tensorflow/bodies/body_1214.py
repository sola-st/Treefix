# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
for dtype in self.numeric_types:
    init = np.array([[[0, 1, 2], [3, 4, 5]], [[10, 11, 12], [13, 14, 15]],
                     [[20, 21, 22], [23, 24j, 25]],
                     [[30, 31, 32], [33, 34, 35]]]).astype(dtype)
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable(init)
        sess.run(variables.variables_initializer([v]))
        x = v.sparse_read([[2, 1], [3, 0]])
        self.assertAllClose(
            np.array(
                [[[[20, 21, 22], [23, 24j, 25]], [[10, 11, 12], [13, 14, 15]]],
                 [[[30, 31, 32], [33, 34, 35]], [[0, 1, 2], [3, 4, 5]]]
                ],).astype(dtype), self.evaluate(x))
