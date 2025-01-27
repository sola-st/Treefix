# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
output = super().to_json()
output.update({
    "host_name": self.host_name,
    "stack_frame_ids": self.stack_frame_ids,
    "tensor_debug_mode": self.tensor_debug_mode,
    "graph_id": self.graph_id,
    "input_tensor_ids": self.input_tensor_ids,
    "output_tensor_ids": self.output_tensor_ids,
    "debug_tensor_values": self.debug_tensor_values,
})
exit(output)
