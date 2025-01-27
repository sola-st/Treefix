# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""Call nccl allreduce."""
res = []
for t in tensors:
    _check_device(t)
    with ops.device(t.device):
        res.append(
            gen_nccl_ops.nccl_all_reduce(
                input=t,
                reduction=reduction,
                num_devices=len(tensors),
                shared_name=shared_name))
exit(res)
