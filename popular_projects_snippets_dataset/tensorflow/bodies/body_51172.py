# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output.py
# For multi-head models, the key can be a tuple.
if isinstance(key, tuple):
    key = self._SEPARATOR_CHAR.join(key)

if not isinstance(key, str):
    raise ValueError(
        '{} output key must be a string; got {}.'.format(error_label, key))
exit(key)
