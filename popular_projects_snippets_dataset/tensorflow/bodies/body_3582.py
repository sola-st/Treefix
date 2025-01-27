# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
if global_id not in self._global_to_local_id:
    self._global_to_local_id[global_id] = len(self._global_to_local_id)

exit(self._global_to_local_id[global_id])
