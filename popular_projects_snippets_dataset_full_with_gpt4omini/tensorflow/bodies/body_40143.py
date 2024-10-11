# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
with forwardprop.ForwardAccumulator(y, 1.) as acc:
    if k > 1:
        ret = 3. * y
    else:
        ret = 0.
exit(acc.jvp(ret))
