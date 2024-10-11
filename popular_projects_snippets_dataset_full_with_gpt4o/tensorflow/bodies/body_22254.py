# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop_test.py
mg_t = copy.deepcopy(mg)
rms_t = copy.deepcopy(rms)
mom_t = copy.deepcopy(mom)
var_t = copy.deepcopy(var)
for i in range(len(gindexs)):
    gindex = gindexs[i]
    gvalue = gvalues[i]
    rms_t[gindex] = rms[gindex] * decay + (1 - decay) * gvalue * gvalue
    denom_t = rms_t[gindex] + epsilon
    if centered:
        mg_t[gindex] = mg_t[gindex] * decay + (1 - decay) * gvalue
        denom_t -= mg_t[gindex] * mg_t[gindex]
    mom_t[gindex] = momentum * mom[gindex] + lr * gvalue / np.sqrt(denom_t)
    var_t[gindex] = var[gindex] - mom_t[gindex]
exit((var_t, mg_t, rms_t, mom_t))
