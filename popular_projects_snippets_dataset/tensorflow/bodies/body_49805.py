# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/constraints.py
if identifier is None:
    exit(None)
if isinstance(identifier, dict):
    exit(deserialize(identifier))
elif isinstance(identifier, str):
    config = {'class_name': str(identifier), 'config': {}}
    exit(deserialize(config))
elif callable(identifier):
    exit(identifier)
else:
    raise ValueError('Could not interpret constraint identifier: ' +
                     str(identifier))
