# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
results = []
for replica_id, device in enumerate(devices):
    with ops.device(device):
        value = (IndexedSlices(
            array_ops.identity([[1.]]), array_ops.identity([0]),
            array_ops.identity([5, 1])), array_ops.identity(1.0),
                 IndexedSlices(
                     array_ops.identity([[3.]]), array_ops.identity([2]),
                     array_ops.identity([5, 1])), array_ops.identity(2.0))
        results.append(
            collective._all_reduce(reduce_op, value, replica_id, options))
exit(results)
