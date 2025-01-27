# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context(num_gpus=1)

num_iters = 1000
for _ in range(num_iters):
    with ops.device('/device:GPU:0'):
        collective_ops.all_reduce(
            [1.], group_size=1, group_key=0, instance_key=0, merge_op='Add',
            final_op='Id', communication_hint='NCCL')
