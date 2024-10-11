# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device
timeout = 1.5
group_key = 20
instance_key = 30
input_data = constant_op.constant([1., 2., 3., 4.])

tokens = {}
for device in [dev0, dev1]:
    with ops.device(device):
        tokens[device] = create_ordering_token()

@def_function.function
def run():
    for device in [dev0, dev1]:
        with ops.device(device):
            collective_op(
                input_data,
                group_size=2,
                group_key=group_key,
                instance_key=instance_key,
                ordering_token=tokens[device],
                communication_hint=communication,
                timeout=timeout)

    # Run a normal all-reduce to complete param resolution.
run()

with self.assertRaisesRegex(errors.DeadlineExceededError,
                            'Collective has timed out during execution'):
    with ops.device(dev0):
        collective_op(
            input_data,
            group_size=2,
            group_key=group_key,
            instance_key=instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication,
            timeout=timeout)

    # We launch the second device after the first device times out. This is to
    # simulate the situation when other workers are slow and the timeout is
    # short. It should error immediately.
with self.assertRaisesRegex(errors.DeadlineExceededError,
                            'Collective has timed out during execution'):
    with ops.device(dev1):
        # No timeout.
        collective_op(
            input_data,
            group_size=2,
            group_key=group_key,
            instance_key=instance_key,
            ordering_token=tokens[dev1],
            communication_hint=communication)
