# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Decorator that compiles a function to use TensorFlow ops.

  The decorator is dynamic - it recompiles the target whenever the decorated
  function is called. This means the parameter values are known at conversion.
  It also means that repeated calls with different types of parameters will be
  correctly processed.

  Args:
    recursive: bool, whether to recursively convert any functions or classes
      that the converted function may use.
    optional_features: converted.Feature, allows toggling optional or
      experimental features. When set to None, only the core features are
      enabled.
    user_requested: bool, whether this is a function that the user explicitly
      asked to be converted. See ConversionOptions.user_requested.
    conversion_ctx: Optional ag_ctx.ControlStatusCtx, the Autograph context in
      which `f` is used.

  Returns:
    Callable, a decorator that converts the given function into an equivalent
    function that uses TensorFlow ops.
  """

def decorator(f):
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

exit(decorator)
