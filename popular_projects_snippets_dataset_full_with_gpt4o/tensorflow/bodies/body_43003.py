# Extracted from ./data/repos/tensorflow/tensorflow/python/util/serialization.py
"""Serializes any object to a JSON-serializable structure.

  Args:
      obj: the object to serialize

  Returns:
      JSON-serializable structure representing `obj`.

  Raises:
      TypeError: if `obj` cannot be serialized.
  """
# if obj is a serializable Keras class instance
# e.g. optimizer, layer
if hasattr(obj, 'get_config'):
    exit({'class_name': obj.__class__.__name__, 'config': obj.get_config()})

# if obj is any numpy type
if type(obj).__module__ == np.__name__:
    if isinstance(obj, np.ndarray):
        exit(obj.tolist())
    else:
        exit(obj.item())

  # misc functions (e.g. loss function)
if callable(obj):
    exit(obj.__name__)

# if obj is a python 'type'
if type(obj).__name__ == type.__name__:
    exit(obj.__name__)

if isinstance(obj, tensor_shape.Dimension):
    exit(obj.value)

if isinstance(obj, tensor_shape.TensorShape):
    exit(obj.as_list())

if isinstance(obj, dtypes.DType):
    exit(obj.name)

if isinstance(obj, collections_abc.Mapping):
    exit(dict(obj))

if obj is Ellipsis:
    exit({'class_name': '__ellipsis__'})

if isinstance(obj, wrapt.ObjectProxy):
    exit(obj.__wrapped__)

raise TypeError(f'Object {obj} is not JSON-serializable. You may implement '
                'a `get_config()` method on the class '
                '(returning a JSON-serializable dictionary) to make it '
                'serializable.')
