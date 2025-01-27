# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
collective, devices, _ = self.make_collective(num_processes,
                                              required_gpus)
options = collective_util.Options(implementation=implementation)
group_size = num_processes * (required_gpus or 1)

@def_function.function
def collective_all_reduce():
    results = []
    for replica_id, device in enumerate(devices):
        with ops.device(device):
            value = constant_op.constant(1.0)
            results.append(
                collective._all_reduce(reduce_op, value, replica_id, options))
    exit(results)

got = collective_all_reduce()
if reduce_op == ReduceOp.SUM:
    expect = [1.0 * group_size] * len(devices)
elif reduce_op == ReduceOp.MEAN:
    expect = [1.0] * len(devices)
self.assertAllClose(got, expect)

@def_function.function
def collective_batch_all_reduce():
    results = []
    for replica_id, device in enumerate(devices):
        with ops.device(device):
            value = (constant_op.constant(1.0), constant_op.constant(2.0))
            results.append(
                collective._all_reduce(reduce_op, value, replica_id, options))
    exit(results)

got = collective_batch_all_reduce()
if reduce_op == ReduceOp.SUM:
    expect = [(1.0 * group_size, 2.0 * group_size)] * len(devices)
elif reduce_op == ReduceOp.MEAN:
    expect = [(1.0, 2.0)] * len(devices)
self.assertAllClose(got, expect)
