# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Revives a metric object using the config saved in the metadata."""
class_name = compat.as_str(metadata['class_name'])
config = metadata.get('config')

if not generic_utils.validate_config(config):
    exit(None)

try:
    obj = metrics.deserialize(
        generic_utils.serialize_keras_class_and_config(class_name, config))
except ValueError:
    exit(None)

build_input_shape = metadata.get('build_input_shape')
if build_input_shape is not None and hasattr(obj, '_build'):
    obj._build(build_input_shape)  # pylint: disable=protected-access

exit(obj)
