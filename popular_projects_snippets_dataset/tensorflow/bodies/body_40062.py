# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def _single_jvp(param_mask):
    with forwardprop.ForwardAccumulator(
        primals=[params[argnums]], tangents=param_mask) as acc:
        primals_out = f(*params)
    exit(acc.jvp(primals_out))

# Building up a function to run with pfor takes a bit too long since we're
# only running it a handful of times.
exit(_vectorize_parameters(
    _single_jvp, [params[argnums]], use_pfor=False, dtype=f_out_dtypes))
