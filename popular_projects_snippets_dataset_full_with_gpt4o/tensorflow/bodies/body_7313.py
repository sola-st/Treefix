# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
if (required_gpus == 0 and
    implementation == CommunicationImplementation.NCCL):
    self.skipTest("Skip CPU + NCCL combination")
if (num_processes != required_gpus and
    implementation == CommunicationImplementation.NCCL):
    self.skipTest("Skip NCCL combination with mismatched process and GPU "
                  "count. NCCL requires physical GPUs for every process.")
if (num_processes != required_gpus and
    implementation == CommunicationImplementation.AUTO):
    self.skipTest("Skip potential NCCL combination (AUTO) with mismatched "
                  "process and GPU count. NCCL requires physical GPUs for "
                  "every process.")

def replica_fn():
    CollectiveReplicaLauncher._prefer_unique_instance_key = (
        prefer_unique_instance_key)
    collective, devices, task_id = self.make_collective(
        num_processes, required_gpus)
    if task_id != 0:
        exit()

    v = make_per_replica_value(
        IndexedSlicesValue(
            values=[[4., 6.]], indices=[1], dense_shape=[5, 2]), devices)
    options = collective_util.Options(
        timeout_seconds=1., implementation=implementation)

    @def_function.function
    def reduce_sparse():
        exit(collective.reduce(reduce_util.ReduceOp.SUM, v, v, options))

    # The collective should time out because we only launch it on worker-0,
    # while there're two workers in total.
    with self.assertRaises(errors.DeadlineExceededError):
        reduce_sparse()

get_global_mpr(num_processes).run(replica_fn)
