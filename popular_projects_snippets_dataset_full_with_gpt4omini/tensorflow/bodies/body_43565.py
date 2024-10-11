# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Decorator that registers a TensorFlow op as a binary elementwise API."""
_BINARY_ELEMENTWISE_APIS.append(func)
for args, handler in _ELEMENTWISE_API_HANDLERS.items():
    if len(args) == 2:
        _add_dispatch_for_binary_elementwise_api(func, args[0], args[1], handler)
exit(func)
