# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
model_dir = self.get_temp_dir()
with strategy.scope():
    m = self.Model()
m.train()
tf.saved_model.save(m, model_dir)

# Load via V2 API.
loaded = tf.saved_model.load(model_dir)
self.assertRegex(loaded.v1.device, "/job:chief/replica:0/task:0")
self.assertRegex(loaded.v2.device, "/job:chief/replica:0/task:0")
self.assertAllEqual(loaded(tf.identity(1)), [6, 6, 6, 6])
loaded.v2.assign([1, 1, 1, 1])
self.assertAllEqual(loaded(tf.identity(1)), [4, 4, 4, 4])

# Load via V1 API.
self.assertAllEqual(self.load_and_run_v1(model_dir, {"x": 1}), [6, 6, 6, 6])
