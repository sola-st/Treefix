# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
coordinator = coordinator_lib.ClusterCoordinator(strategy)
file_path = os.path.join(self.get_temp_dir(), "text_file_initializer")
with strategy.scope():
    model = self.Model(source, file_path)
model_dir = self.get_temp_dir()
tf_save.save(model, model_dir)

if load == "tf_load":
    load_fn = tf_load.load
else:
    load_fn = keras_save.load_model

with strategy.scope():
    loaded = load_fn(model_dir)

loaded_func_captures = (
    loaded.use_table.get_concrete_function().graph.external_captures)
loaded_func_deferred_captures = (
    loaded.use_table.get_concrete_function().graph
    .deferred_external_captures)
# Compared with loading without strategy, there is one less
# external_capture, since the captured table handle has been swapped to a
# closure in the deferred_external_capture
self.assertLen(loaded_func_captures, 1)
self.assertNotEmpty(loaded_func_deferred_captures)

self.assertIsInstance(loaded.table, ps_values.DistributedTable)

self.assertLen([
    t for t in loaded.use_table.get_concrete_function().captured_inputs
    if t.dtype == dtypes.resource
], 1)

self.verifyWorkerLocalInstance(coordinator, loaded)
