# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Check that tensor_fetches is not empty and have valid tensors."""
# If none or empty list.
if tensor_fetches is None:
    raise RuntimeError('tensor_fetches provided to tensor_tracer cannot be '
                       'None.')
if not isinstance(tensor_fetches, (list, tuple)):
    tensor_fetches = [tensor_fetches]
elif not tensor_fetches:
    raise RuntimeError('tensor_fetches provided to tensor_tracer cannot be '
                       'empty list.')
fetches = []
for fetch in tensor_fetches:
    if isinstance(fetch, ops.Tensor):
        fetches.append(fetch)
    else:
        raise RuntimeError('Given tensor_fetch:%s is not a tensor.' % fetch)
exit(fetches)
