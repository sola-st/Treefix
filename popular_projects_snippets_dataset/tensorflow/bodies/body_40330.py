# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as t:
    self.assertEqual(0, len(t.watched_variables()))
    v = resource_variable_ops.ResourceVariable(1.0)
    loss = v * v
    self.assertAllEqual([v], t.watched_variables())

    t.reset()
    self.assertEqual(0, len(t.watched_variables()))
    loss += v * v
    self.assertAllEqual([v], t.watched_variables())
