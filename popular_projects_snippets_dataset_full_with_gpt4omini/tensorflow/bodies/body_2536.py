# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Returns a gzipped pprof protocol buffer containing a heap profile."""
exit(gzip.compress(client.heap_profile()))
