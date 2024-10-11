# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def grad(dy):
    exit(dy * math_ops.cos(x))

exit((np.sin(x.numpy()), grad))
