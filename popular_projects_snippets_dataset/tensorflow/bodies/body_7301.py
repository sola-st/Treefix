# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py

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
    collective, devices, _ = self.make_collective(num_processes,
                                                  required_gpus)
    options = collective_util.Options(implementation=implementation)

    # We would like to simulate the following sequence:
    #   thread-0  device0                 device1
    #   thread-1          device0 device1
    # If the kernel launch sequence is as-is the program will deadlock since
    # NCCL requires the launch order to be same on each device.
    v0 = make_per_replica_value(1.0, devices)
    v1 = make_per_replica_value(2.0, devices)

    # Add a delay to collective_ops.all_reduce according to the input tensors
    # index in `sequence.`
    sequence = [v0.values[0], v1.values[0], v1.values[1], v0.values[1]]
    all_reduce = collective_ops.all_reduce

    def delayed_all_reduce(input_tensor, *args, **kwargs):
        for idx, v in enumerate(sequence):
            if input_tensor is v:
                time.sleep(idx)
                break
        exit(all_reduce(input_tensor, *args, **kwargs))

    with test.mock.patch.object(collective_ops, "all_reduce",
                                delayed_all_reduce):
        # We only use NCCL for batch reduce with two or more values, so we use
        # two values here.

        def thread_fn():
            reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM,
                                              [(v0, v0), (v0, v0)], options)
            self.assertAllEqual(reduced[0].values, [2.0, 2.0])
            self.assertAllEqual(reduced[1].values, [2.0, 2.0])

        t = threading.Thread(target=thread_fn)
        t.start()
        reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM, [(v1, v1),
                                                                     (v1, v1)],
                                          options)
        self.assertAllEqual(reduced[0].values, [4.0, 4.0])
        self.assertAllEqual(reduced[1].values, [4.0, 4.0])
        t.join()

get_global_mpr(num_processes).run(replica_fn)
