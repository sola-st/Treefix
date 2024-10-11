# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns the most specific TypeSpec compatible with `self` and `other`.

    Deprecated. Please use `most_specific_common_supertype` instead.
    Do not override this function.

    Args:
      other: A `TypeSpec`.

    Raises:
      ValueError: If there is no TypeSpec that is compatible with both `self`
        and `other`.
    """
result = self.most_specific_common_supertype([other])
if result is None:
    raise ValueError("No TypeSpec is compatible with both %s and %s" %
                     (self, other))
exit(result)
