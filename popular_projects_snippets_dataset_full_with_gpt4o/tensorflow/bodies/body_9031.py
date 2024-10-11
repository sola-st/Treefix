# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
# `self._inflight_closure_count` only tracks the number of inflight closures
# that are "in generation". Once an error occurs, error generation is
# incremented and all subsequent arriving closures (from inflight) are
# considered "out of generation".
self._inflight_closure_count = 0

self._queue_lock = threading.Lock()

# Condition indicating that all pending closures (either queued or inflight)
# have been processed, failed, or cancelled.
self._stop_waiting_condition = threading.Condition(self._queue_lock)

# Condition indicating that an item becomes available in queue (not empty).
self._closures_queued_condition = threading.Condition(self._queue_lock)
self._should_process_closures = True

# Condition indicating that a queue slot becomes available (not full).
# Note that even with "infinite" queue size, there is still a "practical"
# size limit for the queue depending on host memory capacity, and thus the
# queue will eventually become full with a lot of enqueued closures.
self._queue_free_slot_condition = threading.Condition(self._queue_lock)

# Condition indicating there is no inflight closures.
self._no_inflight_closure_condition = threading.Condition(self._queue_lock)

# Use to cancel in-flight closures.
self._cancellation_mgr = cancellation.CancellationManager()

if _CLOSURE_QUEUE_MAX_SIZE <= 0:
    logging.warning(
        "In a `ClusterCoordinator`, creating an infinite closure queue can "
        "consume a significant amount of memory and even lead to OOM.")
self._queue = queue.Queue(maxsize=_CLOSURE_QUEUE_MAX_SIZE)
self._tagged_queue = collections.defaultdict(queue.Queue)
self._error = None

# The following is a lock to make sure when `wait` is called and before it
# returns no `put` can be executed during this period. It is because `wait`
# won't know what to do with newly put closures. This lock adds an cutoff
# for `wait` so that closures put into the queue while waiting would not be
# taken responsible by this `wait`.
#
# We cannot reuse the `self._queue_lock` since when `wait` waits for a
# condition, the `self._queue_lock` will be released.
#
# We don't use a reader/writer's lock on purpose to reduce the complexity
# of the code.
self._put_wait_lock = threading.Lock()

self._watchdog = watchdog.WatchDog(on_triggered=self._on_watchdog_timeout)
