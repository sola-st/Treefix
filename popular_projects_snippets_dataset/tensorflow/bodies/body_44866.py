# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
self.recursive = recursive
self.user_requested = user_requested
# TODO(mdan): Rename to conversion_recursion_depth?
self.internal_convert_user_code = internal_convert_user_code

if optional_features is None:
    optional_features = ()
elif isinstance(optional_features, Feature):
    optional_features = (optional_features,)
optional_features = frozenset(optional_features)
self.optional_features = optional_features
