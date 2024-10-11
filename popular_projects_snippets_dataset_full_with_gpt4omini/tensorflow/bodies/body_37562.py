# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size = 2
group_key = 100
instance_key = 100

def create_dataset_and_fetch_one(t):
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

@def_function.function
def f():
    with ops.device('CPU:0'):
        value0 = create_dataset_and_fetch_one([1.])
    with ops.device('CPU:1'):
        value1 = create_dataset_and_fetch_one([2.])
    exit((value0, value1))

self.assertAllEqual(self.evaluate(f()), [[3.], [3.]])
