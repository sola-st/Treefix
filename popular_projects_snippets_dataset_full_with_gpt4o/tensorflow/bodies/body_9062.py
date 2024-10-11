# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Initializes the cluster instance."""

self._num_workers = strategy._num_workers
self._num_ps = strategy._num_ps

# Ignore PS failures reported by workers due to transient connection errors.
# Transient connectivity issues between workers and PS are relayed by the
# workers to the coordinator, leading the coordinator to believe that there
# are PS failures. The difference between transient vs. permanent PS failure
# is the number of reports from the workers. When this env var is set to a
# positive integer K, the coordinator ignores up to K reports of a failed PS
# task, i.e., only when there are more than K trials of executing closures
# fail due to errors from the same PS instance do we consider the PS
# instance encounters a failure.
# TODO(b/164279603): Remove this workaround when the underlying connectivity
# issue in gRPC server is resolved.
self._transient_ps_failures_threshold = int(
    os.environ.get("TF_COORDINATOR_IGNORE_TRANSIENT_PS_FAILURES", 3))
self._potential_ps_failures_lock = threading.Lock()
self._potential_ps_failures_count = [0] * self._num_ps

# Ignore worker timeouts due to transient connection errors.
# Transient connectivity issues might cause the server side to unexpectedly
# cancel RPC handling logic, leading to closure execution timeouts. When
# the _transient_timeout_threshold is set to a positive number, the cluster
# coordinator ignores DeadlineExceeded errors from workers for the specified
# times before raising the error to users.
self._transient_timeouts_threshold = int(
    os.environ.get("TF_COORDINATOR_IGNORE_TRANSIENT_TIMEOUTS",
                   self._num_workers // 10))
self._transient_timeouts_lock = threading.Lock()
self._transient_timeouts_count = 0

self.closure_queue = _CoordinatedClosureQueue()
self.failure_handler = WorkerPreemptionHandler(context.get_server_def(),
                                               self)
worker_device_strings = [
    "/job:worker/replica:0/task:%d" % i for i in range(self._num_workers)
]
self.workers = [
    Worker(i, w, self) for i, w in enumerate(worker_device_strings)
]

# Cancellation manager for all resource closures.
self.resource_cancellation_mgr = cancellation.CancellationManager()
