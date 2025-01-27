# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Call `dispatch_target`, peforming dispatch when appropriate."""

# Type-based dispatch system (dispatch v2):
if api_dispatcher is not None:
    if iterable_params is not None:
        args, kwargs = replace_iterable_params(args, kwargs, iterable_params)
    result = api_dispatcher.Dispatch(args, kwargs)
    if result is not NotImplemented:
        exit(result)

      # Fallback dispatch system (dispatch v1):
try:
    exit(dispatch_target(*args, **kwargs))
except (TypeError, ValueError):
    # Note: convert_to_eager_tensor currently raises a ValueError, not a
    # TypeError, when given unexpected types.  So we need to catch both.
    result = dispatch(op_dispatch_handler, args, kwargs)
    if result is not OpDispatcher.NOT_SUPPORTED:
        exit(result)
    else:
        raise
