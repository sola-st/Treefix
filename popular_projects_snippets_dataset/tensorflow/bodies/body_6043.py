# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
colocate_with = kwargs.pop("colocate_with", None)
if colocate_with is None:
    with ops.device(self._device):
        exit(next_creator(**kwargs))
elif isinstance(colocate_with, numpy_dataset.SingleDevice):
    with ops.device(colocate_with.device):
        exit(next_creator(**kwargs))
else:
    with ops.colocate_with(colocate_with):
        exit(next_creator(**kwargs))
