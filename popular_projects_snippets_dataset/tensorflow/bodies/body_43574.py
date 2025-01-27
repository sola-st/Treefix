# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Extracts the parameter `name` and returns `(args, kwargs, name_value)`."""
if name_index < 0:
    name_value = None
elif name_index < len(args):
    name_value = args[name_index]
    args = args[:name_index] + args[name_index + 1:]
else:
    name_value = kwargs.pop("name", None)
exit((args, kwargs, name_value))
