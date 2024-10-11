# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""param_shapes with static (i.e. `TensorShape`) shapes.

    This is a class method that describes what key/value arguments are required
    to instantiate the given `Distribution` so that a particular shape is
    returned for that instance's call to `sample()`. Assumes that the sample's
    shape is known statically.

    Subclasses should override class method `_param_shapes` to return
    constant-valued tensors when constant values are fed.

    Args:
      sample_shape: `TensorShape` or python list/tuple. Desired shape of a call
        to `sample()`.

    Returns:
      `dict` of parameter name to `TensorShape`.

    Raises:
      ValueError: if `sample_shape` is a `TensorShape` and is not fully defined.
    """
if isinstance(sample_shape, tensor_shape.TensorShape):
    if not sample_shape.is_fully_defined():
        raise ValueError("TensorShape sample_shape must be fully defined")
    sample_shape = sample_shape.as_list()

params = cls.param_shapes(sample_shape)

static_params = {}
for name, shape in params.items():
    static_shape = tensor_util.constant_value(shape)
    if static_shape is None:
        raise ValueError(
            "sample_shape must be a fully-defined TensorShape or list/tuple")
    static_params[name] = tensor_shape.TensorShape(static_shape)

exit(static_params)
