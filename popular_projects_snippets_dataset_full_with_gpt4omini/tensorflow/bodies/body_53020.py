# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/utils.py
if (dtype != dtypes.string) and (not dtype.is_integer):
    raise ValueError(
        '{} dtype must be string or integer. dtype: {}.'.format(prefix, dtype))
