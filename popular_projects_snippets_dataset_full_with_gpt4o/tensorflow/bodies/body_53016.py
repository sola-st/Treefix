# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Checks that a config has all expected_keys."""
if set(config.keys()) != set(expected_keys):
    raise ValueError('Invalid config: {}, expected keys: {}'.format(
        config, expected_keys))
