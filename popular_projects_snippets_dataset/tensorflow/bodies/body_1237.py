# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
self.which_mode = 1 - self.which_mode
value = np.array(value).astype(self.dtype)

with self.test.session() as sess, self.test.test_scope():
    x = constant_op.constant(self.x_np, dtype=self.dtype)
    var = resource_variable_ops.ResourceVariable(x)
    sess.run(variables.variables_initializer([var]))

    if self.which_mode == 0:
        val = sess.run(var[index].assign(value))
    else:
        assert self.which_mode == 1
        val = sess.run(state_ops.assign(var[index], value))
    valnp = np.copy(self.x_np)
    valnp[index] = np.array(value)
    self.test.assertAllEqual(val, valnp)
