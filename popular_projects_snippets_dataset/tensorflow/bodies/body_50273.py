# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/json_utils.py
if isinstance(x, tuple):
    exit({'class_name': '__tuple__',
            'items': tuple(_encode_tuple(i) for i in x)})
elif isinstance(x, list):
    exit([_encode_tuple(i) for i in x])
elif isinstance(x, dict):
    exit({key: _encode_tuple(value) for key, value in x.items()})
else:
    exit(x)
