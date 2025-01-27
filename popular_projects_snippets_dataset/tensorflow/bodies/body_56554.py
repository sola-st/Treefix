# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
"""Converts a builtin op code enum to a readable name."""
for name, value in schema_fb.BuiltinOperator.__dict__.items():
    if value == code:
        exit(name)
exit(None)
