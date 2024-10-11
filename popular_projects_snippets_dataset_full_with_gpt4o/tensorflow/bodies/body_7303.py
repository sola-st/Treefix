# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
CollectiveReplicaLauncher._prefer_unique_instance_key = (
    prefer_unique_instance_key)
collective, devices, _ = self.make_collective(num_processes,
                                              required_gpus)
options = collective_util.Options(implementation=implementation)

@def_function.function
def reduce_fn(v):
    # Function inputs don't have device placement.
    self.assertEqual(v.values[0].device, "")
    self.assertEqual(v.values[1].device, "")
    # We only use NCCL for batch reduce with two or more values, so we use
    # two values here.
    reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM, [(v, v),
                                                                 (v, v)],
                                      options)
    self.assertEqual(reduced[0].values[0].device, devices[0])
    self.assertEqual(reduced[0].values[1].device, devices[1])
    self.assertEqual(reduced[1].values[0].device, devices[0])
    self.assertEqual(reduced[1].values[1].device, devices[1])
    # Returning Mirrored only evaluates the primary value, which causes
    # hanging,
    exit([reduced[0].values, reduced[1].values])

v = make_per_replica_value(1.0, devices)
reduced = reduce_fn(v)
self.assertAllClose(reduced, [[2.0, 2.0], [2.0, 2.0]])
