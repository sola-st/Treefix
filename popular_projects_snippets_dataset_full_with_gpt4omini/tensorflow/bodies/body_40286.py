# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
_ = v + 1.0  # This reads the variable inside the loop context
with backprop.GradientTape() as t:
    result = v * 2
self.assertIsNotNone(t.gradient(result, v))
exit(1.0)
