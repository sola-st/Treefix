# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
assert x.flags.f_contiguous, x.strides
# Force the output array to have C layout, which will require a
# transpose back to the expected Fortran layout.
exit((np.ascontiguousarray(x * 2),))
