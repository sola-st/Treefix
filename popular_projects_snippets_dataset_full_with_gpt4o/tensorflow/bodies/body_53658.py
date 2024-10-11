# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""If called, follows NumPy's rules for slicing Tensors.

  Used for enabling NumPy behavior on slicing for TF NumPy.
  """
global _numpy_style_slicing
_numpy_style_slicing = True
