# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    inp = constant(1.0, shape=[100, 32], name="in")
    out = array_ops.stop_gradient(inp)
    igrad = gradients.gradients(out, inp)[0]
assert igrad is None
