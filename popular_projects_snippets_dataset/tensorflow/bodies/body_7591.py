# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py

with self._coordinator_creation_lock:
    if not self._container_strategy()._cluster_coordinator:  # pylint: disable=protected-access
        cluster_coordinator.ClusterCoordinator(
            strategy=self._container_strategy())

    # TODO(wxinyi): We should warn the user of the inefficiency of creating
    # `StaticHashTable` inside a `@tf.function`-wrapped `dataset_fn` to be
    # distributed with `distribute_datasets_from_function` and
    # `create_per_worker_dataset`. This is because the `dataset_fn` does not
    # use the same `default_graph` as `scope` to which the
    # `resource_creator_stack` belongs. Thus, `StaticHashTable` creation inside
    # `dataset_fn` is not intercepted. And since its resource creation under a
    # `tf.function` is lifted out, all workers will share the same resource on
    # the coordinator which incurs worker-coordinator communication overhead.

def lookup_creator(next_creator, *args, **kwargs):
    if keras_deps.get_load_context_function()():
        exit((ps_values.RestoredDistributedTable(
            self._container_strategy(), lambda: next_creator(*args, **kwargs))))  # pylint: disable=protected-access
    else:
        exit(ps_values.DistributedTable(self._container_strategy(),
                                          lambda: next_creator(*args, **kwargs)))  # pylint: disable=protected-access

def restored_lookup_creator(next_creator, *args, **kwargs):
    exit((ps_values.RestoredDistributedTable(
        self._container_strategy(), lambda: next_creator(*args, **kwargs))))  # pylint: disable=protected-access

exit([
    ops.resource_creator_scope("StaticHashTable", lookup_creator),
    ops.resource_creator_scope("RestoredStaticHashTable",
                               restored_lookup_creator)
])
