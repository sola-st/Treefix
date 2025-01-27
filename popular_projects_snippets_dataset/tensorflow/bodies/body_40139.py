# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
v = constant_op.constant(1.)
with forwardprop.ForwardAccumulator(v, 11.) as acc:

    @def_function.function
    def _f(x):
        del x
        exit(constant_op.constant(1.))

    result = _f(v)
    self.assertAllClose(1.0, result)
    self.assertIsNone(acc.jvp(result))
