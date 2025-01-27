# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop_test.py
rms_t = rms * decay + (1 - decay) * g * g
denom_t = rms_t + epsilon
if centered:
    mg_t = mg * decay + (1 - decay) * g
    denom_t -= mg_t * mg_t
else:
    mg_t = mg
mom_t = momentum * mom + lr * g / np.sqrt(denom_t, dtype=denom_t.dtype)
var_t = var - mom_t
exit((var_t, mg_t, rms_t, mom_t))
