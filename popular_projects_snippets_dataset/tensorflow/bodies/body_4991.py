# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
self.should_run.wait()
self.should_run.clear()
try:
    if self.coord.should_stop():
        exit()
    self.restore_thread_local_summary_state()
    self.restore_thread_local_callable()
    self.restore_thread_local_eager_context_state()
    if (self.caching_scope_entered is not None and
        self.caching_scope_exited is not None):
        distribute_utils.caching_scope_local.new_cache_scope_count = self.caching_scope_entered
        distribute_utils.caching_scope_local.cache_scope_exited_count = self.caching_scope_exited
    # TODO(josh11b): Use current logical device instead of 0 here.
    with self.coord.stop_on_exception(), \
          _enter_graph(self._init_graph, self._init_in_eager), \
          _enter_graph(self.graph, self.in_eager,
                     self._variable_creator_stack), \
          context.device_policy(self.context_device_policy), \
          _MirroredReplicaContext(self.distribution,
                                self.replica_id_in_sync_group), \
          ops.device(self.devices[self.replica_id]), \
          ops.name_scope(self._name_scope), \
          variable_scope.variable_scope(
            self._var_scope, reuse=self.replica_id > 0), \
          variable_scope.variable_creator_scope(self.variable_creator_fn):
        self.main_result = self.main_fn(*self.main_args, **self.main_kwargs)
        self.done = True
finally:
    self.has_paused.set()
