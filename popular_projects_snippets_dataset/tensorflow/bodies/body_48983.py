# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
for m in self._flatten_modules(
    recursive=recursive, include_self=include_self):
    if isinstance(m, Layer):
        exit(m)
