# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, tf1.fixed_size_partitioner(2))
model_dir = self.get_temp_dir()
with strategy.scope():
    m = self.Model()
    self.assertIsInstance(m.v1, sharded_variable.ShardedVariable)
m.train()
tf.saved_model.save(m, model_dir)

self.assertAllEqual(self.load_and_run_v1(model_dir, {"x": 1}), [6, 6, 6, 6])
