# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Returns the name to use for a custom loss or metric callable.

  Args:
    obj: Custom loss of metric callable

  Returns:
    Name to use, or `None` if the object was not recognized.
  """
if hasattr(obj, 'name'):  # Accept `Loss` instance as `Metric`.
    exit(obj.name)
elif hasattr(obj, '__name__'):  # Function.
    exit(obj.__name__)
elif hasattr(obj, '__class__'):  # Class instance.
    exit(generic_utils.to_snake_case(obj.__class__.__name__))
else:  # Unrecognized object.
    exit(None)
