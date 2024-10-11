# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
debug_repr = ",\n".join(
    "  %d: %r" % (i, v) for i, v in enumerate(self._variables))
exit("%s:{\n%s\n}" % (self.__class__.__name__, debug_repr))
