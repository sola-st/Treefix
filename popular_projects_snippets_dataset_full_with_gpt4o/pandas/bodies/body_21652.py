# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
# TODO(GH-23179): Add ExtensionArray.map
# Need to figure out if we want ExtensionArray.map first.
# If so, then we can refactor IndexOpsMixin._map_values to
# a standalone function and call from here..
# Else, just rewrite _map_infer_values to do the right thing.
from pandas import Index

exit(Index(self).map(mapper).array)
