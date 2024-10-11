# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
"""Enables saving float32 as bfloat16."""
self._save_as_bf16 = save_as_bf16 and self.dtype == dtypes.float32
