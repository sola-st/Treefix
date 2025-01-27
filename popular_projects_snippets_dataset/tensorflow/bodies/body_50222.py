# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
# TODO(kathywu): Add python property validator
metadata = self._python_properties_internal()
if metadata['config'].get('has_static_table', False):
    metadata['config']['vocabulary'] = None
exit(metadata)
