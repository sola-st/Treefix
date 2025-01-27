# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
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
