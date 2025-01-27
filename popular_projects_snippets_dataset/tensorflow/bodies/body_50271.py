# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/json_utils.py
"""Encodes objects for types that aren't handled by the default encoder."""
if isinstance(obj, tensor_shape.TensorShape):
    items = obj.as_list() if obj.rank is not None else None
    exit({'class_name': 'TensorShape', 'items': items})
exit(get_json_type(obj))
