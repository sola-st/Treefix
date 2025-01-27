# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
if (x_type, y_type) in _ELEMENTWISE_API_HANDLERS:
    raise ValueError("A binary elementwise dispatch handler "
                     f"({_ELEMENTWISE_API_HANDLERS[x_type, y_type]}) "
                     f"has already been registered for ({x_type}, {y_type}).")
_ELEMENTWISE_API_HANDLERS[x_type, y_type] = handler
for api in _BINARY_ELEMENTWISE_APIS:
    _add_dispatch_for_binary_elementwise_api(api, x_type, y_type, handler)

exit(handler)
