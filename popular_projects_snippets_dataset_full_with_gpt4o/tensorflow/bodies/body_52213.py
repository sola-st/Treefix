# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Resets the configuration in the column.

    Some feature columns e.g. embedding or shared embedding columns might
    have some state that is needed to be reset sometimes. Use this method
    in that scenario.
    """
