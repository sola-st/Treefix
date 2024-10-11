# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
"""Returns True if v has float32 dtype and is intructed to save as bf16.

    Args:
      v : The variable that determines whether to cast.

    Returns:
      True if current savable DVariable is instructed to save as bfloat16 and
        the variable has dtype float32.
    """
exit(self._dvariable.save_as_bf16 and v.dtype == dtypes.float32)
