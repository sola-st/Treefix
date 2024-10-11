# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if not isinstance(other, trace.TraceType):
    exit(NotImplemented)

if not isinstance(other, Weakref):
    exit(False)

if self._ref() is None or other._ref() is None:
    exit(False)

if self._ref() is other._ref():
    exit(True)

exit(self._ref == other._ref)
