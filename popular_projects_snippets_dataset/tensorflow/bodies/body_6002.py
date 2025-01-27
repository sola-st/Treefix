# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py

file_path = os.path.join(self.get_temp_dir(), "text_file_initializer")

model = self.Model(source, file_path)
func_captures = model.use_table.get_concrete_function(
).graph.external_captures
self.assertLen(func_captures, 2)
self.assertTrue(
    any(model.table.resource_handle is t for t in func_captures))
deferred_captures = model.use_table.get_concrete_function(
).graph.deferred_external_captures
self.assertEmpty(deferred_captures)

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
coordinator = coordinator_lib.ClusterCoordinator(strategy)
with strategy.scope():
    distributed_model = self.Model("value", file_path)
func_captures = distributed_model.use_table.get_concrete_function(
).graph.external_captures
# One less external_capture, since the table handle becomes a closure in the
# deferred_external_capture
self.assertLen(func_captures, 1)
self.assertFalse(
    any(model.table.resource_handle is t for t in func_captures))
deferred_captures = distributed_model.use_table.get_concrete_function(
).graph.deferred_external_captures
self.assertNotEmpty(deferred_captures)

self.verifyWorkerLocalInstance(coordinator, distributed_model)
