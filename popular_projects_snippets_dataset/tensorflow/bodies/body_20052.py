# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Validate `feature_to_config_dict`."""
used_table_set = set(
    [feature.table_id for feature in feature_to_config_dict.values()])
table_set = set(table_to_config_dict.keys())

unused_table_set = table_set - used_table_set
if unused_table_set:
    raise ValueError(
        '`table_to_config_dict` specifies table that is not '
        'used in `feature_to_config_dict`: {}.'.format(unused_table_set))

extra_table_set = used_table_set - table_set
if extra_table_set:
    raise ValueError(
        '`feature_to_config_dict` refers to a table that is not '
        'specified in `table_to_config_dict`: {}.'.format(extra_table_set))
