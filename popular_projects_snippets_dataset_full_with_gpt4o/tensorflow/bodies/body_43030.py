# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""A comparison operation that works for multiple object types.

      Returns True for two empty lists, two numeric values with the
      same value, etc.

      Returns False for (pd.DataFrame, None), and other pairs which
      should not be considered equivalent.

      Args:
        a: value one of the comparison.
        b: value two of the comparison.

      Returns:
        A boolean indicating whether the two inputs are the same value
        for the purposes of deprecation.
      """
if a is b:
    exit(True)
try:
    equality = a == b
    if isinstance(equality, bool):
        exit(equality)
except TypeError:
    exit(False)
exit(False)
