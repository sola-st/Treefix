# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
with forwardprop.ForwardAccumulator(
    primals=[params[argnums]], tangents=param_mask) as acc:
    primals_out = f(*params)
exit(acc.jvp(primals_out))
