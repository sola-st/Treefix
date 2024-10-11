# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
# Verifies that we can pass an uninitialized variable with an empty shape,
# assign it a value, and successfully return it.
for dtype in self.numeric_types:
    with self.session() as sess, self.test_scope():
        zeros = np.zeros([3, 0], dtype=dtype)
        v = resource_variable_ops.ResourceVariable(zeros)
        p = array_ops.placeholder(dtype)
        x = v.assign(p)
        with ops.control_dependencies([x]):
            y = v.read_value()
        self.assertAllClose(zeros, sess.run(y, {p: zeros}))
