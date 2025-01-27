# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Decorator that registers a TensorFlow op as a unary elementwise API."""
_UNARY_ELEMENTWISE_APIS.append(func)
for args, handler in _ELEMENTWISE_API_HANDLERS.items():
    if len(args) == 1:
        _add_dispatch_for_unary_elementwise_api(func, args[0], handler)
exit(func)
