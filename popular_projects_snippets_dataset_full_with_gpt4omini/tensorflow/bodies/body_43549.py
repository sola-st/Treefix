# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
if name_index < len(args):
    name = args[name_index]
    args = args[:name_index] + args[name_index + 1:]
else:
    name = kwargs.pop("name", None)
if name is None:
    exit(func(*args, **kwargs))
else:
    with ops.name_scope(name):
        exit(func(*args, **kwargs))
