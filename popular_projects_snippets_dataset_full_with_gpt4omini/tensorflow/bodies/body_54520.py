# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Applies the given device only if device is not None or empty."""
if device:
    with ops.device(device):
        exit()
else:
    exit()
