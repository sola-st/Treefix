# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values_test.py
with distribution.scope():
    aggregating = variables_lib.Variable(1.)
self.assertIsInstance(aggregating, ps_values.AggregatingVariable)
self.evaluate(aggregating.assign(3.))
self.assertEqual(self.evaluate(aggregating.read_value()), 3.)
self.assertEqual(self.evaluate(aggregating._v.read_value()), 3.)
