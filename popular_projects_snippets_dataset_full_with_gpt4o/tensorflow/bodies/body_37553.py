# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
for device in [dev0, dev1]:
    with ops.device(device):
        collective_op(
            input_data,
            group_size=2,
            group_key=group_key,
            instance_key=instance_key,
            ordering_token=tokens[device],
            communication_hint='NCCL')
