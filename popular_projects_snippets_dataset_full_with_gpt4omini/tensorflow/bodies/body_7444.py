# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
if convert_callable:
    init_value = init_value()
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
with strategy.scope():
    v = variables.Variable(init_value)

self.assertIsInstance(v, d_variable.DVariable)
self.assertIsNotNone(v.layout)
self.assertEqual(v.layout, layout.Layout.replicated(self.mesh, rank=1))
