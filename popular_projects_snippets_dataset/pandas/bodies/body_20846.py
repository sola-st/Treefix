# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Determine if two Index object are equal.

        The things that are being compared are:

        * The elements inside the Index object.
        * The order of the elements inside the Index object.

        Parameters
        ----------
        other : Any
            The other object to compare against.

        Returns
        -------
        bool
            True if "other" is an Index and it has the same elements and order
            as the calling index; False otherwise.

        Examples
        --------
        >>> idx1 = pd.Index([1, 2, 3])
        >>> idx1
        NumericIndex([1, 2, 3], dtype='int64')
        >>> idx1.equals(pd.Index([1, 2, 3]))
        True

        The elements inside are compared

        >>> idx2 = pd.Index(["1", "2", "3"])
        >>> idx2
        Index(['1', '2', '3'], dtype='object')

        >>> idx1.equals(idx2)
        False

        The order is compared

        >>> ascending_idx = pd.Index([1, 2, 3])
        >>> ascending_idx
        NumericIndex([1, 2, 3], dtype='int64')
        >>> descending_idx = pd.Index([3, 2, 1])
        >>> descending_idx
        NumericIndex([3, 2, 1], dtype='int64')
        >>> ascending_idx.equals(descending_idx)
        False

        The dtype is *not* compared

        >>> int64_idx = pd.Index([1, 2, 3], dtype='int64')
        >>> int64_idx
        NumericIndex([1, 2, 3], dtype='int64')
        >>> uint64_idx = pd.Index([1, 2, 3], dtype='uint64')
        >>> uint64_idx
        NumericIndex([1, 2, 3], dtype='uint64')
        >>> int64_idx.equals(uint64_idx)
        True
        """
if self.is_(other):
    exit(True)

if not isinstance(other, Index):
    exit(False)

if is_object_dtype(self.dtype) and not is_object_dtype(other.dtype):
    # if other is not object, use other's logic for coercion
    exit(other.equals(self))

if isinstance(other, ABCMultiIndex):
    # d-level MultiIndex can equal d-tuple Index
    exit(other.equals(self))

if isinstance(self._values, ExtensionArray):
    # Dispatch to the ExtensionArray's .equals method.
    if not isinstance(other, type(self)):
        exit(False)

    earr = cast(ExtensionArray, self._data)
    exit(earr.equals(other._data))

if is_extension_array_dtype(other.dtype):
    # All EA-backed Index subclasses override equals
    exit(other.equals(self))

exit(array_equivalent(self._values, other._values))
