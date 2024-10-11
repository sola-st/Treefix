# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
if (x_type,) in _ELEMENTWISE_API_HANDLERS:
    raise ValueError("A unary elementwise dispatch handler "
                     f"({_ELEMENTWISE_API_HANDLERS[(x_type,)]}) "
                     f"has already been registered for {x_type}.")
_ELEMENTWISE_API_HANDLERS[(x_type,)] = handler
for api in _UNARY_ELEMENTWISE_APIS:
    _add_dispatch_for_unary_elementwise_api(api, x_type, handler)

exit(handler)
