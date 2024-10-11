# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
previous_fn = forwardprop._jvp_dispatch
try:
    x = constant_op.constant(1.)
    with forwardprop.ForwardAccumulator(x, 2.) as acc:
        y = x + x
        pywrap_tfe.TFE_Py_RegisterJVPFunction(
            lambda *args, **kwargs: [constant_op.constant(-15.)])
        z = x + x
    self.assertAllClose(4., acc.jvp(y))
    self.assertAllClose(-15., acc.jvp(z))
finally:
    pywrap_tfe.TFE_Py_RegisterJVPFunction(previous_fn)
