# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
if not self.has_placeholder(alias_id):
    raise KeyError(f"alias_id: {alias_id} not found in this instance of "
                   "placeholder context.")
exit(self._alias_id_to_placeholder[alias_id])
