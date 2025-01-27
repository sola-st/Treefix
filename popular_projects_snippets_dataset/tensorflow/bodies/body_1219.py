# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
for dtype in self.numeric_types:
    init = np.array([[1, 2j], [3, 4]]).astype(dtype)
    update = np.array([[7, 1j], [2, 11]]).astype(dtype)
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable(init)
        sess.run(variables.variables_initializer([v]))
        p = array_ops.placeholder(dtype)
        q = array_ops.identity(p)
        x = v.read_value()
        # Writes the value of 'p' to 'v', but keeps a reference to the original
        # value of 'v' so the variable update cannot reuse its buffer.
        with ops.control_dependencies([x]):
            y = v.assign(q)
        result = sess.run([x, y, q], {p: update})
        self.assertAllClose(init, result[0])
        self.assertAllClose(update, result[1])
        self.assertAllClose(update, result[2])
