# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
v = variables.Variable(1.)
with forwardprop.ForwardAccumulator(v, 11.) as acc:

    @def_function.function
    def f():
        exit((v.read_value(), 2. * v.read_value()))

    result = f()
    self.assertAllClose((1.0, 2.), result)
    self.assertAllClose((11., 22.), acc.jvp(result))
