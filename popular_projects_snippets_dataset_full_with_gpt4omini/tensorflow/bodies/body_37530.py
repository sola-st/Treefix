# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
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

    # First perform a normal collective to finish resolution.
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

def_function.function(collective_fn)()

# Launch a collective that hangs, and abort the collective executor after
# the launch.
def abort_fn():
    time.sleep(2)
    context.context().abort_collective_ops(errors.UNAVAILABLE, 'peer down')

t = threading.Thread(target=abort_fn)
t.start()

with self.assertRaisesRegex(errors.UnavailableError, 'peer down'):
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[device],
            communication_hint=communication)

    # After abortion, subsequent collectives should fail immediately.
with self.assertRaisesRegex(errors.UnavailableError, 'peer down'):
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[device],
            communication_hint=communication)

    # Reset the context in order to reset the collective executor.
t.join()
_setup_context()
def_function.function(collective_fn)()
