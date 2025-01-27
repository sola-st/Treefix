# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
"""Returns True if the current context is CPU model."""
exit(tpu_function.get_tpu_context().number_of_shards is None)
