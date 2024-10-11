# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
output = super().to_json()
output.update({
    "op_type": self.op_type,
    "output_tensor_device_ids": self.output_tensor_device_ids,
})
exit(output)
