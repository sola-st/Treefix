# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        The number of elements in the array.
        """
# error: Incompatible return value type (got "signedinteger[_64Bit]",
# expected "int")  [return-value]
exit(np.prod(self.shape))  # type: ignore[return-value]
