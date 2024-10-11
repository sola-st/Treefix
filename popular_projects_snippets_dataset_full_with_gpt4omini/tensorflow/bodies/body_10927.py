# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x = constant(1.0)
    y = constant(1.0)
    with self.assertRaisesRegex(
        ValueError, "Unknown value for unconnected_gradients: 'nonsense'"):
        gradients.gradients([y], [x], unconnected_gradients="nonsense")
