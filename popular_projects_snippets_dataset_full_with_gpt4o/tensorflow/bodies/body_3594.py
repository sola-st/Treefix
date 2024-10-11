# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
if not self.has_handledata(spec_id):
    raise KeyError("Could not find handle data for TraceType with "
                   f"id: {spec_id} in this instance of placeholder context.")
exit(self._spec_id_to_handledata[spec_id])
