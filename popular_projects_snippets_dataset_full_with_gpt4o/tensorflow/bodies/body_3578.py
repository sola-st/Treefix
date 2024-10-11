# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
if self._triggered:
    on_delete()
else:
    self._callables.append(on_delete)
