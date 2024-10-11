# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py
if communication == "NCCL":
    self.skipTest("b/171358086: cannot test multi worker NCCL")
dev0 = "/device:%s:0" % device
cluster_resolver = cluster_resolver_lib.TFConfigClusterResolver()
enable_collective_ops_with_barrier(cluster_resolver)
group_size = 2
group_key = 100
instance_key = 100
in_tensor = constant_op.constant([1.])

# First perform a normal all-reduce to complete the group resolution.
with ops.device(dev0):
    collective_ops.all_reduce(in_tensor, group_size, group_key, instance_key)

# We use broadcast to test aborting instance resolution since only broadcast
# waits for the group.

if cluster_resolver.task_id == 1:

    def abort_fn():
        time.sleep(2)
        context.context().abort_collective_ops(errors.UNAVAILABLE, "peer down")

    t = threading.Thread(target=abort_fn)
    t.start()

    # Use a different instance key to trigger another instance resolution.
    instance_key = 101
    with self.assertRaisesRegex(errors.UnavailableError, "peer down"):
        # This hangs on params resolution since we're only launching one
        # collective for a group size of 2.
        with ops.device(dev0):
            collective_ops.broadcast_send(in_tensor, (1,), dtypes.float32,
                                          group_size, group_key, instance_key)

      # After abortion, subsequent collectives should fail immediately.
    with self.assertRaisesRegex(errors.UnavailableError, "peer down"):
        with ops.device(dev0):
            collective_ops.broadcast_send(in_tensor, (1,), dtypes.float32,
                                          group_size, group_key, instance_key)

    t.join()

# Enable collective ops again in order to reset the collective executor.
enable_collective_ops_with_barrier(cluster_resolver)
# Reassign instance_key so that it's the same on each worker.
instance_key = 100
with ops.device(dev0):
    if cluster_resolver.task_id == 0:
        collective_ops.broadcast_send(in_tensor, (1,), dtypes.float32,
                                      group_size, group_key, instance_key)
    else:
        collective_ops.broadcast_recv((1,), dtypes.float32, group_size,
                                      group_key, instance_key)
