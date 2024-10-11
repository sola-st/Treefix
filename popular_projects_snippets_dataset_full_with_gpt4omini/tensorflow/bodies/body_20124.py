# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Sets the type of each element of the queue.

    tuple_types must be a list of length
    self.number_of_tuple_elements, and each element must be
    convertible to a dtype.

    Args:
      tuple_types: the types of each queue element.

    Raises:
      ValueError: if tuple_types is not of length
        self.number_of_tuple_elements.
      TypeError: if an element of tuple_types cannot be converted to a
        dtype.
    """
if len(tuple_types) != self.number_of_tuple_elements:
    raise ValueError(
        f"tuple_types is {str(tuple_types)}, but must be a list of "
        f"length {self.number_of_tuple_elements}"
    )
if self._frozen:
    for (frozen, updated) in zip(self._tuple_types, tuple_types):
        if frozen != updated:
            raise ValueError(
                "Trying to update InfeedQueue with frozen configuration with an "
                f"incompatible type. Frozen types are {str(self._tuple_types)}, "
                f"updated types are {str(tuple_types)}")
else:
    try:
        self._tuple_types = [dtypes.as_dtype(t) for t in tuple_types]
    except (TypeError) as e:
        raise TypeError(
            f"tuple_types is {str(tuple_types)}, but must be a list of "
            f"elements each convertible to dtype: got error {str(e)}") from e
