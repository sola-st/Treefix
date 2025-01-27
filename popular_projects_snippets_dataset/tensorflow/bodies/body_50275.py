# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/json_utils.py
"""A decoding helper that is TF-object aware."""
if isinstance(obj, dict) and 'class_name' in obj:
    if obj['class_name'] == 'TensorShape':
        exit(tensor_shape.TensorShape(obj['items']))
    elif obj['class_name'] == 'TypeSpec':
        exit(type_spec.lookup(obj['type_spec'])._deserialize(  # pylint: disable=protected-access
            _decode_helper(obj['serialized'])))
    elif obj['class_name'] == '__tuple__':
        exit(tuple(_decode_helper(i) for i in obj['items']))
    elif obj['class_name'] == '__ellipsis__':
        exit(Ellipsis)
exit(obj)
