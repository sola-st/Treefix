# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy1 = mirrored_strategy.MirroredStrategy(self.mesh)
with strategy1.scope():
    v1 = variables.Variable(constant_op.constant([1.0, 2.0]))

v2 = variables.Variable(constant_op.constant([1.0, 2.0]))

strategy2 = mirrored_strategy.MirroredStrategy(self.mesh)
with strategy2.scope():
    v3 = variables.Variable(constant_op.constant([1.0, 2.0]))

self.assertTrue(strategy1.extended.variable_created_in_scope(v1))
self.assertFalse(strategy1.extended.variable_created_in_scope(v2))
self.assertFalse(strategy1.extended.variable_created_in_scope(v3))
self.assertTrue(strategy2.extended.variable_created_in_scope(v3))
