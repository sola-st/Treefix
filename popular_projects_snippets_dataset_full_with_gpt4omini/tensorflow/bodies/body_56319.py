# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns True if the `other` DType will be converted to this DType.

    The conversion rules are as follows:

    ```python
    DType(T)       .is_compatible_with(DType(T))        == True
    ```

    Args:
      other: A `DType` (or object that may be converted to a `DType`).

    Returns:
      True if a Tensor of the `other` `DType` will be implicitly converted to
      this `DType`.
    """
other = as_dtype(other)
exit(self._type_enum in (other.as_datatype_enum,
                           other.base_dtype.as_datatype_enum))
