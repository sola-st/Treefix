# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
# This test simulates the case when a worker fails before or during reducing
# a small tensors, e.g. reading a metric.
#
# Note that this is written for a specific corner case that used to happen
# only when all of the following conditions are met:
#   - There're two workers.
#   - They're reducing a small tensor. The definition of small varies
#     per platform.
#   - They're reducing a single tensor. Batched all-reduce are not affected.
#   - It must be worker-1 that fails.
# Under this case, the all-reduce is effectively two send/recv operation,
# the first one from worker-0 to worker-1, and the second one vice versa.
# The first one blocks the second one. In send/recv, the sending party is
# not aware of the failures of the receiving party.

def worker_fn():
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    value = tf.identity([1.])
    strategy.reduce("sum", value, axis=None)
    # worker-1 dies here.
    if strategy.cluster_resolver.task_id == 1:
        quick_exit(1)
    strategy.reduce("sum", value, axis=None)

cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
mpr = multi_process_runner.MultiProcessRunner(
    worker_fn, cluster_spec, rpc_layer=RPC_PROTOCOL)
mpr.start()
# TODO(b/151232436): Always raise UnavailableError when a peer fails.
with self.assertRaises(
    (tf.errors.UnavailableError, tf.errors.DeadlineExceededError)):
    mpr.join(timeout=60)
