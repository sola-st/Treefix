# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
# We need to support slashes in local names for compatibility, since this
# naming scheme is being patched in to things like Layer.add_variable where
# slashes were previously accepted. We also want to use slashes to indicate
# edges traversed to reach the variable, so we escape forward slashes in
# names.
exit((name.replace(_ESCAPE_CHAR, _ESCAPE_CHAR + _ESCAPE_CHAR).replace(
    r"/", _ESCAPE_CHAR + "S")))
