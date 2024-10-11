# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
args, kwargs, name = _extract_name_arg(args, kwargs, name_index)
if len(args) > 1:
    x, y, args = args[0], args[1], args[2:]
elif args:
    x, args = args[0], args[1:]
    y = kwargs.pop(y_name, None)
else:
    x = kwargs.pop(x_name, None)
    y = kwargs.pop(y_name, None)

if need_to_bind_api_args:
    tensor_api = lambda v1, v2: api(v1, v2, *args, **kwargs)
else:
    tensor_api = api

if name is None:
    exit(elementwise_api_handler(tensor_api, x, y))
else:
    with ops.name_scope(name, None, [x, y]):
        exit(elementwise_api_handler(tensor_api, x, y))
