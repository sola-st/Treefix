# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# Use a dummy all-reduce as a barrier to wait for all workers to be up,
# otherwise the check health may fail immediately.

# Use array_ops.identity to create the dummy tensor so that we have a new
# Tensor. If we use constant it may be a cached from on a /job:localhost
# device, which will cause some code that relies on tensor.device to error.
#
# TODO(b/151232436): change to an explicit barrier if we have it.
dummy_value = array_ops.identity([])
logging.info("Waiting for the cluster, timeout = %s",
             self._check_health_initial_timeout or "inf")
try:
    self._host_cross_device_ops.reduce(
        reduce_util.ReduceOp.SUM,
        dummy_value,
        dummy_value,
        options=collective_util.Options(
            timeout_seconds=self._check_health_initial_timeout,
            implementation=collective_util.CommunicationImplementation.RING))
    if context.is_async():
        context.async_wait()
except errors.DeadlineExceededError:
    raise RuntimeError(
        "Timeout waiting for the cluster, timeout is %d seconds" %
        self._check_health_initial_timeout)
logging.info("Cluster is ready.")
self._check_health_thread_should_stop = threading.Event()
# Start the thread as daemon to avoid it blocking the program from exiting.
# We try best to shutdown the thread but __del__ is not guaranteed to be
# called when program exists.
self._check_health_thread = threading.Thread(
    target=self._check_health,
    daemon=True)
self._check_health_thread.start()
