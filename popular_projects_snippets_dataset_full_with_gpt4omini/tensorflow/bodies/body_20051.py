# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Validate `table_to_config_dict`."""
for k, v in table_to_config_dict.items():
    if not isinstance(v, TableConfig):
        raise ValueError('Value of `table_to_config_dict` must be of type '
                         '`TableConfig`, got {} for {}.'.format(type(v), k))
