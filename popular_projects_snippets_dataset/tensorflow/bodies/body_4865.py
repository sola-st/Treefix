# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
model_dir = self.get_temp_dir()
with strategy.scope():
    m = self.Model()
m.train()
tf.saved_model.save(m, model_dir)

with strategy.scope():
    loaded = tf.saved_model.load(model_dir)

# Make sure that the variables are created on different devices. SavedModel
# may load the variables in a different order compared to the creation order
# so the devices may not be exactly the same as before.
self.assertTrue(("/job:ps/replica:0/task:0" in loaded.v1.device and
                 "/job:ps/replica:0/task:1" in loaded.v2.device) or
                ("/job:ps/replica:0/task:1" in loaded.v1.device and
                 "/job:ps/replica:0/task:0" in loaded.v2.device))
self.assertAllEqual(loaded(tf.identity(1)), [6, 6, 6, 6])
