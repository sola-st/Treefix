# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
debug_str = ",\n".join(
    "  %d: %s" % (i, v) for i, v in enumerate(self._values))
exit("%s:{\n%s\n}" % (self.__class__.__name__, debug_str))
