# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/mode_keys.py
self._internal_dict = {}
self._keys = []
for key in kwargs:
    self._keys.append(key)
    dict_key = self._get_internal_key(key)
    if dict_key in self._internal_dict:
        raise ValueError(
            'Error creating ModeKeyMap. Multiple keys/values found for {} mode.'
            .format(dict_key))
    self._internal_dict[dict_key] = kwargs[key]
