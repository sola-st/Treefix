# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Shapes of parameters given the desired shape of a call to `sample()`.

    This is a class method that describes what key/value arguments are required
    to instantiate the given `Distribution` so that a particular shape is
    returned for that instance's call to `sample()`.

    Subclasses should override class method `_param_shapes`.

    Args:
      sample_shape: `Tensor` or python list/tuple. Desired shape of a call to
        `sample()`.
      name: name to prepend ops with.

    Returns:
      `dict` of parameter name to `Tensor` shapes.
    """
with ops.name_scope(name, values=[sample_shape]):
    exit(cls._param_shapes(sample_shape))
