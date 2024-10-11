# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
output = super().to_json()
output.update({
    "graph_ids": self.graph_ids,
    "tensor_debug_mode": self.tensor_debug_mode,
    "debug_tensor_value": self.debug_tensor_value,
    "device_name": self.device_name,
})
exit(output)
