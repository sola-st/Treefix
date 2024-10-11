# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context(num_gpus=2)

group_size = 2
group_key = 100
instance_key = 100
in_tensor = constant_op.constant(1.)

# First perform a normal collective to finish resolution.
def collective_fn():
    for device in ['GPU:0', 'GPU:1']:
        with ops.device(device):
            collective_ops.all_reduce(
                in_tensor,
                group_size,
                group_key,
                instance_key,
                'Add',
                'Id',
                communication_hint='nccl')

def_function.function(collective_fn)()

# Launch a collective that hangs, and abort the collective executor after
# the launch.
def abort_fn():
    time.sleep(2)
    context.context().abort_collective_ops(errors.UNAVAILABLE, 'peer down')

t = threading.Thread(target=abort_fn)
t.start()

with self.assertRaisesRegex(errors.UnavailableError, 'peer down'):
    collective_ops.all_reduce(
        in_tensor,
        group_size,
        group_key,
        instance_key,
        'Add',
        'Id',
        communication_hint='nccl')

# After abortion, subsequent collectives should fail immediately.
with self.assertRaisesRegex(errors.UnavailableError, 'peer down'):
    collective_ops.all_reduce(
        in_tensor,
        group_size,
        group_key,
        instance_key,
        'Add',
        'Id',
        communication_hint='nccl')

t.join()
# Reset the context in order to reset the collective executor.
context._reset_context()  # pylint: disable=protected-access
def_function.function(collective_fn)()
