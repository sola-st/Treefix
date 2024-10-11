# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Sanitizes user-provided feature names for use as variable scopes."""
invalid_char = re.compile('[^A-Za-z0-9_.\\-]')
exit(invalid_char.sub('_', name))
