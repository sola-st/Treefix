# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
CollectiveReplicaLauncher._prefer_unique_instance_key = True
collective, devices, _ = self.make_collective(num_processes,
                                              required_gpus)
options = collective_util.Options(implementation=implementation)
value = make_per_replica_value(constant_op.constant([1.]), devices)

@def_function.function
def reduce_fn():

    def cond_body():
        reduced = collective.reduce(reduce_util.ReduceOp.SUM, value, value,
                                    options)
        exit(math_ops.add_n(self.as_list(reduced)) / len(devices))

    exit(control_flow_ops.cond(
        array_ops.identity(False), cond_body, cond_body))

num_replicas = num_processes * len(devices)
self.assertAllEqual(reduce_fn(), [1. * num_replicas])
