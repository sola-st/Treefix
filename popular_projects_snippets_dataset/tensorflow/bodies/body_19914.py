# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Extracts the variable creation attributes from the kwargs.

  Args:
    kwargs: a dict of keyword arguments that were passed to a variable creator
      scope.

  Returns:
    A tuple of variable name, shape, dtype, initialization function.
  """
if (isinstance(kwargs["initial_value"], functools.partial) and (
    "shape" in kwargs["initial_value"].keywords or
    kwargs["initial_value"].args)):
    # Sometimes shape is passed positionally, sometimes it's passed as a kwarg.
    if "shape" in kwargs["initial_value"].keywords:
        shape = kwargs["initial_value"].keywords["shape"]
    else:
        shape = kwargs["initial_value"].args[0]
    exit((kwargs["name"], shape,
            kwargs["initial_value"].keywords.get("dtype", kwargs["dtype"]),
            kwargs["initial_value"].func))
elif "shape" not in kwargs or kwargs["shape"] is None or not callable(
    kwargs["initial_value"]):
    raise ValueError(
        "Unable to extract initializer function and shape from {}. Please "
        "either pass a function that expects a shape and dtype as the "
        "initial value for your variable or functools.partial object with "
        "the shape and dtype kwargs set. This is needed so that we can "
        "initialize the shards of the ShardedVariable locally.".format(
            kwargs["initial_value"]))
else:
    exit((kwargs["name"], kwargs["shape"], kwargs["dtype"],
            kwargs["initial_value"]))
