# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py

if num_processes != required_gpus:
    self.skipTest("Skip NCCL combination with mismatched process and GPU "
                  "count. NCCL requires physical GPUs for every process.")

def replica_fn():
    CollectiveReplicaLauncher._prefer_unique_instance_key = True
    CollectiveReplicaLauncher._prefer_ordering_token = True
    collective, devices, _ = self.make_collective(num_processes,
                                                  required_gpus)
    options = collective_util.Options(
        implementation=CommunicationImplementation.NCCL)

    v_dense = make_per_replica_value([1.0, 1.0], devices)
    v_sparse = make_per_replica_value([
        IndexedSlicesValue([[4., 6.], [5., 6.]], [1, 3], [5, 2]),
        IndexedSlicesValue([[4., 6.], [5., 6.]], [1, 3], [5, 2]),
    ], devices)

    @def_function.function
    def nested_dense():
        collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)

    @def_function.function
    def nested_sparse():
        collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)

    # All collectives, function calls, if clause and while loops should be
    # chained by control dependencies, so that the execution order is
    # deterministic.
    @def_function.function
    def f():
        # pylint: disable=pointless-statement
        collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)
        # reducing dense value.
        collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
        # reducing sparse value.
        collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)
        # reduce dense value in nested tf.function.
        nested_dense()
        # reduce sparse value in nested tf.function.
        nested_sparse()
        # reduce dense value in tf.cond.
        if array_ops.identity(1.0) > array_ops.identity(2.0):
            collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
        else:
            v_dense
        # reduce sparse value in tf.cond.
        if array_ops.identity(1.0) > array_ops.identity(2.0):
            v_sparse
        else:
            collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse,
                              options)
        # reduce dense value in tf.while_loop.
        i = array_ops.identity(1)
        while i < 3:
            collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
            i += 1
        # reduce sparse value in tf.while_loop.
        i = array_ops.identity(1)
        while i < 3:
            collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse,
                              options)
            i += 1
        # reducing dense and sparse value again.
        collective.reduce(reduce_util.ReduceOp.SUM, v_dense, v_dense, options)
        collective.reduce(reduce_util.ReduceOp.SUM, v_sparse, v_sparse, options)
        # pylint: enable=pointless-statement

    graph = f.get_concrete_function().graph
    should_be_ordered = set([
        "CollectiveReduceV2", "CollectiveGatherV2", "If", "While",
        "StatefulPartitionedCall"
    ])
    nodes_by_device = {}
    for op in graph.get_operations():
        if op.type in should_be_ordered:
            if op.device not in nodes_by_device:
                nodes_by_device[op.device] = []
            nodes_by_device[op.device].append(op)
    order = test_util.topological_sort_operations(graph.get_operations())
    for device in devices:
        device = device_util.canonicalize(device)
        # Those function ops don't have device annotations, but they contain
        # collectives for both devices so we always include them.
        operations = nodes_by_device[device] + nodes_by_device[""]
        # Verify that we get all types of nodes we want.
        self.assertEqual(set(op.type for op in operations), should_be_ordered)
        test_util.assert_sequential_execution(order, operations)

get_global_mpr(num_processes).run(replica_fn)
