# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
e = math_ops.exp(x)

def grad(dy):
    exit(dy * e)  # incorrect to check the custom gradients is respected.

exit((math_ops.log(1 + e), grad))
