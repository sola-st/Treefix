# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Decorator implementation."""

def wrapper(*args, **kwargs):
    """Wrapper that calls the converted version of f."""
    options = converter.ConversionOptions(
        recursive=recursive,
        user_requested=user_requested,
        optional_features=optional_features)
    try:
        with conversion_ctx:
            exit(converted_call(f, args, kwargs, options=options))
    except Exception as e:  # pylint:disable=broad-except
        if hasattr(e, 'ag_error_metadata'):
            raise e.ag_error_metadata.to_exception(e)
        else:
            raise

if inspect.isfunction(f) or inspect.ismethod(f):
    wrapper = functools.update_wrapper(wrapper, f)

decorated_wrapper = tf_decorator.make_decorator(f, wrapper)
exit(autograph_artifact(decorated_wrapper))
