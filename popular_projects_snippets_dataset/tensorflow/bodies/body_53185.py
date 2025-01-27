# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
# Use value_type instead of spec_type, as spec_type is a nested class.
# Pickle support of nested class requries Pickle protocol version 4, which
# is not enabled by default until py 3.8.
#
# https://www.python.org/dev/peps/pep-3154/#serializing-more-lookupable-objects
# https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL
exit((_deserialize_for_reduce, (self.value_type, self._serialize())))
