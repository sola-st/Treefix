# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
try:
    original_setting = def_function.functions_run_eagerly()
    def_function.run_functions_eagerly(True)
    x = constant_op.constant(1.)
    with forwardprop.ForwardAccumulator(x, 2.) as acc:
        y = x * 3.
    self.assertAllClose(6., acc.jvp(y))
finally:
    def_function.run_functions_eagerly(original_setting)
