# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Abort v1 collective ops if there're active collective ops at the time of
# an op error. This is due to the inability to cancel collective ops, and op
# errors may cause running collective ops to hang.
dev0 = '/device:%s:0' % device
group_size = 2
group_key = 100
instance_key = 100
in_tensor = constant_op.constant([1.])
# Make the dataset sleep a while so that the collective is being executed
# when the EOF happens.
dataset = dataset_ops.Dataset.from_tensors([1.]).apply(
    dataset_testing.sleep(sleep_microseconds=200))

tokens = {}
for device in [dev0]:
    with ops.device(device):
        tokens[device] = create_ordering_token()

@def_function.function
def f():
    # Launch a collective op that won't be able to finish to test abortion
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
# Now collective ops is aborted, subsequent collective ops should fail with
# the previous error.
with self.assertRaises(errors.CancelledError):
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication)
