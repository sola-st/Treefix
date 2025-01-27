# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    zero_size_var = variables.Variable(array_ops.zeros([0, 2]))
    zero_size_const = array_ops.ones([2, 0])
    variable_mul = math_ops.matmul(zero_size_const, zero_size_var)
    const_mul = math_ops.matmul(
        zero_size_const, zero_size_const, transpose_b=True)
    self.evaluate(variables.global_variables_initializer())
    variable_output = self.evaluate(variable_mul)
    self.assertAllClose(self.evaluate(const_mul), variable_output)
    self.assertAllClose([[0., 0.], [0., 0.]], variable_output)
