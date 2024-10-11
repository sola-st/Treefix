# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
value = 0
abs_value = 0
shape = [3, 3, 10, 10]
count = 70
tol = 1e-5
with self.session():
    for i in range(count):
        x = variable_scope.get_variable(
            "{}".format(i),
            shape=shape,
            initializer=init_ops.convolutional_delta_orthogonal)
        self.evaluate(x.initializer)
        y = self.evaluate(x)[1, 1, :, :]
        determinant = np.linalg.det(y)
        value += determinant
        abs_value += np.abs(determinant)

    # Check there is some variation in the signs of the determinants
    self.assertLess(value, count - tol)
    self.assertLess(-count + tol, value)
    # Check all determinants have absolute value 1
    # Compute the sum of the absolute values of 'count' determinants
    self.assertAllClose(abs_value, count, rtol=tol, atol=tol)
