# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
var_creator = self._create_var_creator(next_creator, **kwargs)

if "colocate_with" in kwargs:
    colocate_with = kwargs["colocate_with"]
    if isinstance(colocate_with, numpy_dataset.SingleDevice):
        with ops.device(colocate_with.device):
            exit(var_creator(**kwargs))
    with ops.device(None):
        with ops.colocate_with(colocate_with):
            exit(var_creator(**kwargs))

with ops.colocate_with(None, ignore_existing=True):
    with ops.device(self._variable_device):
        exit(var_creator(**kwargs))
