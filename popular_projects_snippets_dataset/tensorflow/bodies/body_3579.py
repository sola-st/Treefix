# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
self._triggered = True
for c in self._callables:
    c()
