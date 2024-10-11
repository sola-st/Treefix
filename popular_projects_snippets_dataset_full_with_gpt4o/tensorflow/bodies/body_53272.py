# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a hashable eq-comparable key for `self`."""
# TODO(b/133606651): Decide whether to cache this value.
exit((type(self), self.__make_cmp_key(self._serialize())))
