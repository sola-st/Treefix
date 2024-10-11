# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
model_dir = self.get_temp_dir()
with strategy.scope():
    m = self.Model()
m.train()
tf.saved_model.save(m, model_dir)

del m  # Garbage collect variables before we reset the context.
context._reset_context()

mirrored_strategy = tf.distribute.MirroredStrategy(devices=["CPU:0"])
with mirrored_strategy.scope():
    loaded = tf.saved_model.load(model_dir)
self.assertIsInstance(loaded.v1, values.DistributedVariable)
self.assertAllEqual(loaded(tf.identity(1)), [6, 6, 6, 6])
