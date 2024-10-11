# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
args, kwargs, name = _extract_name_arg(args, kwargs, name_index)
if args:
    x, args = args[0], args[1:]
else:
    x = kwargs.pop(x_name)

if need_to_bind_api_args:
    tensor_api = lambda v: api(v, *args, **kwargs)
else:
    tensor_api = api

if name is None:
    exit(elementwise_api_handler(tensor_api, x))
else:
    with ops.name_scope(name, None, [x]):
        exit(elementwise_api_handler(tensor_api, x))
