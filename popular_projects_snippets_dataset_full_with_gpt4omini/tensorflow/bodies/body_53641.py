# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
self._exit_fns.pop()(type_arg, value_arg, traceback_arg)
exit(False)  # False values do not suppress exceptions
