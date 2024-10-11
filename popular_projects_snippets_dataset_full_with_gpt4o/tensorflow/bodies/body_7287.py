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
    collective, devices, _ = self.make_collective(num_processes,
                                                  required_gpus)
    options = collective_util.Options(implementation=implementation)
    group_size = num_processes * (required_gpus or 1)

    @def_function.function
    def collective_all_reduce():
        results = []
        for replica_id, device in enumerate(devices):
            with ops.device(device):
                value = IndexedSlices(
                    values=array_ops.identity([[1.]]),
                    indices=array_ops.identity([0]),
                    dense_shape=array_ops.identity([5, 1]))
                results.append(
                    collective._all_reduce(reduce_op, value, replica_id, options))
        exit(results)

    got = collective_all_reduce()
    if reduce_op == ReduceOp.SUM:
        expect = [IndexedSlices([[1. * group_size]], [0], [5, 1])
                 ] * len(devices)
    elif reduce_op == ReduceOp.MEAN:
        expect = [IndexedSlices([[1.]], [0], [5, 1])] * len(devices)
    self.assertAllClose(
        nest.map_structure(ops.convert_to_tensor, got),
        nest.map_structure(ops.convert_to_tensor, expect))

    @def_function.function
    def collective_batch_all_reduce():
        results = []
        for replica_id, device in enumerate(devices):
            with ops.device(device):
                value = (IndexedSlices(
                    array_ops.identity([[1.]]), array_ops.identity([0]),
                    array_ops.identity([5, 1])),
                         IndexedSlices(
                             array_ops.identity([[3.]]), array_ops.identity([2]),
                             array_ops.identity([5, 1])))
                results.append(
                    collective._all_reduce(reduce_op, value, replica_id, options))
        exit(results)

    got = collective_batch_all_reduce()
    if reduce_op == ReduceOp.SUM:
        expect = [(IndexedSlices([[1. * group_size]], [0], [5, 1]),
                   IndexedSlices([[3. * group_size]], [2], [5, 1]))
                 ] * len(devices)
    elif reduce_op == ReduceOp.MEAN:
        expect = [(IndexedSlices([[1.]], [0], [5, 1]),
                   IndexedSlices([[3.]], [2], [5, 1]))] * len(devices)
    self.assertAllClose(
        nest.map_structure(ops.convert_to_tensor, got),
        nest.map_structure(ops.convert_to_tensor, expect))

get_global_mpr(num_processes).run(replica_fn)
