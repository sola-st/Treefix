# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as t:
    x = resource_variable_ops.ResourceVariable(1.0)
    x2 = x * 2  # This should be differentiated through.
    with t.stop_recording():
        y = x2 * x2
    z = x2 * x2
self.assertEqual(t.gradient(y, x2), None)

# If the x*2 was not differentiated through, this would be 2.0, not 4.0
self.assertEqual(t.gradient(z, x2).numpy(), 4.0)
