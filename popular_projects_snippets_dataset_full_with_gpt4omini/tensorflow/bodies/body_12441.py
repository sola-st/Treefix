# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""The shared name of the variable.

      Unlike name(), shared_name doesn't have ":0" suffix. It is user-specified
      name with name scope prefix.

    Returns:
      variable name.
    """
exit(self.name[:self.name.index(":")])
