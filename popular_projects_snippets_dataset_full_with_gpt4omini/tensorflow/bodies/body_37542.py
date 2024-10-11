# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Do not abort v2 collective ops even if there're active collective ops at
# the time of an op error. We rely cancellation to terminate active
# collective ops.
dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device
group_size = 2
group_key = 100
instance_key = 100
in_tensor = constant_op.constant([1.])

tokens = {}
for device in [dev0, dev1]:
    with ops.device(device):
        tokens[device] = create_ordering_token()

@def_function.function
def collective_fn():
    for device in [dev0, dev1]:
        with ops.device(device):
            collective_op(
                in_tensor,
                group_size,
                group_key,
                instance_key,
                ordering_token=tokens[device],
                communication_hint=communication)

    # Local params resolution cannot be cancelled yet, so we perform a normal
    # collective so that the group is resolved.
collective_fn()

# Make the dataset sleep a while so that the collective is being executed
# when the EOF happens.
dataset = dataset_ops.Dataset.from_tensors([1.]).apply(
    dataset_testing.sleep(sleep_microseconds=200))

@def_function.function
def f():
    # Launch a collective op that won't be able to finish to test cancellation
    # when other ops error.
    with ops.device(dev0):
        ret = collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication)
    iterator = iter(dataset)
    next(iterator)
    # This should raise EOF.
    next(iterator)
    exit(ret)

with self.assertRaises(errors.OutOfRangeError):
    f()
# Collective ops shouldn't be aborted and new collectives should be able to
# proceed.
collective_fn()
