# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""If called, follows NumPy's rules for type promotion.

  Used for enabling NumPy behavior on methods for TF NumPy.
  """
global _numpy_style_type_promotion
_numpy_style_type_promotion = True
