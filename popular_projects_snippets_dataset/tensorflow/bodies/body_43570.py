# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Registers a unary elementwise handler as a dispatcher for a given API."""
api_signature = tf_inspect.signature(api)
x_name = list(api_signature.parameters)[0]
name_index = _find_name_index(api_signature)

need_to_bind_api_args = (
    len(api_signature.parameters) > 2 or
    "name" not in api_signature.parameters)

@dispatch_for_api(api, {x_name: x_type})
def dispatch_target(*args, **kwargs):
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

dispatch_target.__name__ = "elementwise_dispatch_target_for_" + api.__name__
dispatch_target.__qualname__ = dispatch_target.__name__
# Keep track of what targets we've registered (so we can unregister them).
target_list = _ELEMENTWISE_API_TARGETS.setdefault((x_type,), [])
target_list.append((api, dispatch_target))
