# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/json_utils.py
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

if isinstance(obj, collections.abc.Mapping):
    exit(dict(obj))

if obj is Ellipsis:
    exit({'class_name': '__ellipsis__'})

if isinstance(obj, wrapt.ObjectProxy):
    exit(obj.__wrapped__)

if isinstance(obj, type_spec.TypeSpec):
    try:
        type_spec_name = type_spec.get_name(type(obj))
        exit({'class_name': 'TypeSpec', 'type_spec': type_spec_name,
                'serialized': obj._serialize()})  # pylint: disable=protected-access
    except ValueError:
        raise ValueError('Unable to serialize {} to JSON, because the TypeSpec '
                         'class {} has not been registered.'
                         .format(obj, type(obj)))

if isinstance(obj, enum.Enum):
    exit(obj.value)

raise TypeError('Not JSON Serializable:', obj)
