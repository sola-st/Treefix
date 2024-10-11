# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([t])

def reduce_fn(t):
    # A token is created for each device.
    token = create_ordering_token()
    exit(CollectiveOpsV2.all_reduce(
        t,
        group_size=group_size,
        group_key=group_key,
        instance_key=instance_key,
        ordering_token=token))

dataset = dataset.map(reduce_fn)
exit(next(iter(dataset)))
