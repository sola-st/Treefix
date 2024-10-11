# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
if alias_id in self._alias_id_to_placeholder:
    raise KeyError(f"alias id: {alias_id} is already stored in this "
                   "instance of placeholder context.")
self._alias_id_to_placeholder[alias_id] = placeholder
