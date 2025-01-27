# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    var = resource_variable_ops.ResourceVariable(1.0, name="var")

    @def_function.function
    def Foo():
        y = math_ops.multiply(var, 2.0, name="y")
        g = gradients_impl.gradients(y, var)
        exit(g[0])

    f = Foo()

    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(self.evaluate(f), 2.0)
