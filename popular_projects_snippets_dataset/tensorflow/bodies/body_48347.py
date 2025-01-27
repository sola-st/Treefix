# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Dedupe weights while maintaining order as much as possible."""
output, seen_ids = [], set()
for w in weights:
    if id(w) not in seen_ids:
        output.append(w)
        # Track the Variable's identity to avoid __eq__ issues.
        seen_ids.add(id(w))

exit(output)
