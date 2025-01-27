# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
# Tests bug where int attributes >= 2**31 raised an exception on platforms
# where sizeof(long) = 32 bits.
ctx = context.context()
ctx.ensure_initialized()
shape = constant_op.constant([10])
minval = constant_op.constant(0)
maxval = constant_op.constant(10)
seed = 2**50
pywrap_tfe.TFE_Py_FastPathExecute(ctx, "RandomUniformInt", None,
                                  shape, minval, maxval,
                                  "seed", seed)
