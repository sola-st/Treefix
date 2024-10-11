# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
"""The variable dtype of this policy.

    This is the dtype layers will create their variables in, unless a layer
    explicitly chooses a different dtype. If this is different than
    `Policy.compute_dtype`, Layers will cast variables to the compute dtype to
    avoid type errors.

    Variable regularizers are run in the variable dtype, not the compute dtype.

    Returns:
      The variable dtype of this policy, as a string.
    """
exit(self._variable_dtype)
