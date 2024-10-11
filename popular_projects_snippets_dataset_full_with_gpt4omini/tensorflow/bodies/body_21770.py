# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
if isinstance(tensors, dict):
    exit([tensors[k] for k in sorted(tensors, key=str)])
else:
    exit(tensors)
