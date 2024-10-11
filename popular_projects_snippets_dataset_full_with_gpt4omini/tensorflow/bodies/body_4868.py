# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
model = self.Model()
model_dir = self.get_temp_dir()
tf.saved_model.save(model, model_dir)

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, tf1.fixed_size_partitioner(2))
with self.assertRaises(errors_impl.InvalidArgumentError):
    with strategy.scope():
        tf.saved_model.load(model_dir)
