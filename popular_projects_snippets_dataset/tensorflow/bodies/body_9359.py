# Extracted from ./data/repos/tensorflow/tensorflow/python/types/trace.py
"""Returns the most specific supertype of `self` and `others`, if exists.

    The returned `TraceType` is a supertype of `self` and `others`, that is,
    they are all subtypes (see `is_subtype_of`) of it.
    It is also most specific, that is, there it has no subtype that is also
    a common supertype of `self` and `others`.

    If `self` and `others` have no common supertype, this returns `None`.

    Args:
     others: A sequence of TraceTypes.

    Example:
    ```python
     class Dimension(TraceType):
       def __init__(self, value: Optional[int]):
         self.value = value

       def most_specific_common_supertype(self, other):
          # Either the value is the same or other has a generalized value that
          # can represent any specific ones.
          if self.value == other.value:
            return self.value
          else:
            return Dimension(None)
    ```
    """
