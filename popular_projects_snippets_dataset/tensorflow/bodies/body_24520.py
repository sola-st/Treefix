# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
output = super().to_json()
output.update({
    "graph_id": self.graph_id,
    "op_type": self.op_type,
    "op_name": self.op_name,
    "output_tensor_ids": self.output_tensor_ids,
    "host_name": self.host_name,
    "stack_frame_ids": self.stack_frame_ids,
    "input_names": self.input_names,
    "device_name": self.device_name,
})
exit(output)
