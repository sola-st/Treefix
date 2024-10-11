# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
overload = self._overload_of(op)
if overload is None:
    exit(self._as_binary_operation(op, left, right))
exit(self._as_binary_function(overload, left, right))
