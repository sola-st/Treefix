# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
file_path = os.path.join(self.get_temp_dir(), "text_file_initializer")
with strategy.scope():
    model = self.Model(source, file_path)

model_dir = self.get_temp_dir()
tf_save.save(model, model_dir)

if load == "tf_load":
    load_fn = tf_load.load
else:
    load_fn = keras_save.load_model

loaded_without_strategy = load_fn(model_dir)
loaded_func_captures_without_strategy = (
    loaded_without_strategy.use_table.get_concrete_function().graph
    .external_captures)
loaded_func_deferred_captures_without_strategy = (
    loaded_without_strategy.use_table.get_concrete_function().graph
    .deferred_external_captures)
self.assertLen(loaded_func_captures_without_strategy, 2)
self.assertEmpty(loaded_func_deferred_captures_without_strategy)

self.assertAllEqual(
    loaded_without_strategy.use_table(
        constant_op.constant([0, 1, 3], dtype=dtypes.int64)), [0, 1, -2])
