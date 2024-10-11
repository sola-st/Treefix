# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Converts a numerical enum to a readable tensor type."""
for name, value in schema_fb.TensorType.__dict__.items():
    if value == tensor_type:
        exit(name)
exit(None)
