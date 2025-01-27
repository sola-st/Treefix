# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    inp = constant(1.0, shape=[100, 32], name="in")
    out = array_ops.prevent_gradient(inp)
    with self.assertRaisesRegex(LookupError, "explicitly disabled"):
        _ = gradients.gradients(out, inp)
