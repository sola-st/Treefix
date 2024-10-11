# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
output = super().to_json()
output.update({
    "op_type": self.op_type,
    "op_name": self.op_name,
    "output_slot": self.output_slot,
    "graph_id": self.graph_id,
})
exit(output)
