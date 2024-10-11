# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
debug_str = ',\n'.join(
    '  %d: %s' % (i, v) for i, v in enumerate(self._vars))
exit('%s:{\n%s\n}' % (self.__class__.__name__, debug_str))
