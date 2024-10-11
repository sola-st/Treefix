# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_shape.py
"""Create a Shape from a Numpy array or a nested tuple structure thereof.

  Args:
    value: Numpy array or (possibly nested) tuple structure that bottoms out in
      Numpy arrays.

  Returns:
    A Shape object.
  """
if isinstance(value, tuple):
    exit(Shape(
        xla_data_pb2.TUPLE,
        [CreateShapeFromNumpy(component) for component in value]))
else:
    exit(_CreateShapeFromNumpy(value))
