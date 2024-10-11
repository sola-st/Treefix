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

def abort_fn():
    time.sleep(2)
    context.context().abort_collective_ops(errors.UNAVAILABLE, 'peer down')

t = threading.Thread(target=abort_fn)
t.start()

with self.assertRaisesRegex(errors.UnavailableError, 'peer down'):
    # This hangs on params resolution since we're only launching one
    # collective for a group size of 2.
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication)

    # After abortion, subsequent collectives should fail immediately.
with self.assertRaisesRegex(errors.UnavailableError, 'peer down'):
    with ops.device(dev0):
        collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            ordering_token=tokens[dev0],
            communication_hint=communication)

t.join()
# Reset the context in order to reset the collective executor.
_setup_context()

# After reset non-NCCL collectives should work.
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
