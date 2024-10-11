# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
"""Convenience wrapper to create Numpy arrays with a np.float32 dtype."""
exit(np.array(*args, dtype=np.float32, **kwargs))
