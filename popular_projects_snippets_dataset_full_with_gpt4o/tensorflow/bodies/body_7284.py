# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
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
