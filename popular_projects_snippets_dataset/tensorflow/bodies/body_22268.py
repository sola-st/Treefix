# Extracted from ./data/repos/tensorflow/tensorflow/python/training/localhost_cluster_performance_test.py
workers, _ = test.create_local_cluster(num_workers=1, num_ps=100)
worker_sessions = [session_lib.Session(w.target) for w in workers]
worker = worker_sessions[0]
partition_sizes = (1, 512, 1024 * 32, 1024 * 128)

partitioned = []

for partition_size in partition_sizes:
    # max_shard_bytes is 4, shape is 1000*partition_size float32s which should
    # partition into 1000 shards, each containing partition_size float32s.
    print("Building partitioned variable with %d floats per partition" %
          partition_size)
    with ops.device(device_setter.replica_device_setter(ps_tasks=100)):
        partitioned_ix = variable_scope.get_variable(
            "partitioned_%d" % partition_size,
            shape=[1000 * partition_size],
            dtype=dtypes.float32,
            # Each partition to have exactly N float32s
            partitioner=partitioned_variables.variable_axis_size_partitioner(
                max_shard_bytes=4 * partition_size))
        # Concatenates along axis 0
        partitioned.append(ops.convert_to_tensor(partitioned_ix))

variables.global_variables_initializer().run(session=worker)

for ix, partition_size in enumerate(partition_sizes):
    print("Running benchmark having partitions with %d floats" %
          partition_size)
    self.run_op_benchmark(
        worker,
        partitioned[ix],
        name=("read_concat_1000_partitions_from_"
              "100_parameter_servers_partsize_%d_floats" % partition_size))
