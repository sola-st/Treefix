# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
results = []
for replica_id, device in enumerate(devices):
    with ops.device(device):
        value = constant_op.constant(1.0)
        results.append(
            collective._all_reduce(reduce_op, value, replica_id, options))
exit(results)
