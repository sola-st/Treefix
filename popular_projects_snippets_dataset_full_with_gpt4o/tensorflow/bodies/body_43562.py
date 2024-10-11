# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
api_handler_key = (x_type, y_type, _ASSERT_API_TAG)
if api_handler_key in _ELEMENTWISE_API_HANDLERS:
    raise ValueError("A binary elementwise assert dispatch handler "
                     f"({_ELEMENTWISE_API_HANDLERS[api_handler_key]}) "
                     f"has already been registered for ({x_type}, {y_type}).")
_ELEMENTWISE_API_HANDLERS[api_handler_key] = handler
for api in _BINARY_ELEMENTWISE_ASSERT_APIS:
    _add_dispatch_for_binary_elementwise_api(api, x_type, y_type, handler)

exit(handler)
