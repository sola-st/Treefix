# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# Do not abort if there's no active collective ops. There could be
# exceptions like EOF which we expect users to catch, aborting collective
# ops on all op errors intervenes with this workflow.
dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device
group_size = 2
group_key = 100
instance_key = 100
dataset = dataset_ops.Dataset.from_tensors([1.])
tokens = {}
for device in [dev0, dev1]:
    with ops.device(device):
        tokens[device] = create_ordering_token()

@def_function.function
def collective_fn(in_tensor):
    for device in [dev0, dev1]:
        with ops.device(device):
            collective_op(
                in_tensor,
                group_size,
                group_key,
                instance_key,
                communication_hint=communication,
                ordering_token=tokens[device])

@def_function.function
def f():
    iterator = iter(dataset)
    collective_fn(next(iterator))
    # This next(iterator) should raise EOF.
    collective_fn(next(iterator))

collective_fn(constant_op.constant([1.]))
with self.assertRaises(errors.OutOfRangeError):
    f()
collective_fn(constant_op.constant([1.]))
