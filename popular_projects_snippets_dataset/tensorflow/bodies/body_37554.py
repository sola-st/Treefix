# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
# communication_hint=NCCL should work for CPU by falling back to RING. The
# test doesn't actually require GPU, only GPU builds. We specify
# required_gpus=1 so that it's tested with GPU builds.
dev0 = '/device:CPU:0'
dev1 = '/device:CPU:1'
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
                communication_hint='NCCL')

run()
