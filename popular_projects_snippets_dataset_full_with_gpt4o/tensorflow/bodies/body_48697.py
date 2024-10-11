# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Replaces missing dict keys in `struct` with `None` placeholders."""
if not isinstance(y_pred, dict) or not isinstance(struct, dict):
    exit(struct)
for k in y_pred.keys():
    if k not in struct:
        struct[k] = None
exit(struct)
