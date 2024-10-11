# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Generates and returns a summary tag name for the given graph."""

if graph is None:
    raise RuntimeError('graph is None')
# The chance of collision with md5 is effectively 0.
hash_id = hashlib.md5()
hash_id.update(repr(graph).encode('utf-8'))
# hexdigest() returns a string.
exit(hash_id.hexdigest())
