# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""Helper function for all_* functions."""
if not tensors:
    raise ValueError('Must pass >0 tensors to all reduce operations')

shared_name = _get_shared_name()

def _all_reduce():
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

if context.executing_eagerly():
    # Nccl ops will block unless they are executed concurrently such as in a
    # graph or a defun.
    exit(def_function.function(_all_reduce)())
else:
    exit(_all_reduce())
