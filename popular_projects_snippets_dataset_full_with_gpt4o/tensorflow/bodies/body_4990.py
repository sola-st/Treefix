# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
super(_MirroredReplicaThread, self).__init__()
self.coord = coord
self.distribution = dist
self.devices = devices
self.replica_id = replica_id
self.replica_id_in_sync_group = (
    dist.extended._get_replica_id_in_sync_group(replica_id))  # pylint: disable=protected-access

self.variable_creator_fn = variable_creator_fn
# State needed to run and return the results of `fn`.
self.main_fn = fn
self.main_args = args
self.main_kwargs = kwargs
self.main_result = None
self.done = False
# State needed to run the next merge_call() (if any) requested via
# ReplicaContext.
self.merge_fn = None
self.merge_args = None
self.merge_kwargs = None
self.merge_result = None
self.captured_name_scope = None
self.captured_var_scope = None
try:
    self.caching_scope_entered = caching_scope.new_cache_scope_count
    self.caching_scope_exited = caching_scope.cache_scope_exited_count
except AttributeError:
    self.caching_scope_entered = None
    self.caching_scope_exited = None

# We use a thread.Event for the main thread to signal when this
# thread should start running (`should_run`), and another for
# this thread to transfer control back to the main thread
# (`has_paused`, either when it gets to a
# `get_replica_context().merge_call` or when `fn` returns). In
# either case the event starts cleared, is signaled by calling
# set(). The receiving thread waits for the signal by calling
# wait() and then immediately clearing the event using clear().
self.should_run = threading.Event()
self.has_paused = threading.Event()
# These fields have to do with inheriting various contexts from the
# parent thread:
context.ensure_initialized()
ctx = context.context()
self.in_eager = ctx.executing_eagerly()
self.record_thread_local_summary_state()
self.record_thread_local_eager_context_state()
self.context_device_policy = (
    pywrap_tfe.TFE_ContextGetDevicePlacementPolicy(
        ctx._context_handle))  # pylint: disable=protected-access
self.graph = ops.get_default_graph()
with ops.init_scope():
    self._init_in_eager = context.executing_eagerly()
    self._init_graph = ops.get_default_graph()
self._variable_creator_stack = self.graph._variable_creator_stack[:]  # pylint: disable=protected-access
self._var_scope = variable_scope.get_variable_scope()
# Adding a "/" at end lets us re-enter this scope later.
self._name_scope = self.graph.get_name_scope()
if self._name_scope:
    self._name_scope += "/"
if self.replica_id > 0:
    if not self._name_scope:
        self._name_scope = ""
    self._name_scope += "replica_%d/" % self.replica_id

self._thread_local_callables = thread_local_callables
