# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Variables on TPU have a few restrictions."""
partitioner = kwargs.get("partitioner", None)
if partitioner is not None:
    kwargs["partitioner"] = None
    logging.warning(
        "Partitioned variables are not supported on TPU. Got "
        "`partitioner` that is %s for variable %s. "
        "Setting `partitioner` to `None`.", partitioner, name)
if saved_custom_getter is None:
    exit(getter(name, *args, **kwargs))
else:
    exit(saved_custom_getter(getter, name, *args, **kwargs))
