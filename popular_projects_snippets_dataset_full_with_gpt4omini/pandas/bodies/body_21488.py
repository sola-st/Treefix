# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""Set one or more values inplace.

        Parameters
        ----------
        key : int, ndarray, or slice
            When called from, e.g. ``Series.__setitem__``, ``key`` will be
            one of

            * scalar int
            * ndarray of integers.
            * boolean ndarray
            * slice object

        value : ExtensionDtype.type, Sequence[ExtensionDtype.type], or object
            value or values to be set of ``key``.

        Returns
        -------
        None
        """
# GH50085: unwrap 1D indexers
if isinstance(key, tuple) and len(key) == 1:
    key = key[0]

key = check_array_indexer(self, key)
value = self._maybe_convert_setitem_value(value)

if com.is_null_slice(key):
    # fast path (GH50248)
    data = self._if_else(True, value, self._data)

elif is_integer(key):
    # fast path
    key = cast(int, key)
    n = len(self)
    if key < 0:
        key += n
    if not 0 <= key < n:
        raise IndexError(
            f"index {key} is out of bounds for axis 0 with size {n}"
        )
    if is_list_like(value):
        raise ValueError("Length of indexer and values mismatch")
    elif isinstance(value, pa.Scalar):
        value = value.as_py()
    chunks = [
        *self._data[:key].chunks,
        pa.array([value], type=self._data.type, from_pandas=True),
        *self._data[key + 1 :].chunks,
    ]
    data = pa.chunked_array(chunks).combine_chunks()

elif is_bool_dtype(key):
    key = np.asarray(key, dtype=np.bool_)
    data = self._replace_with_mask(self._data, key, value)

elif is_scalar(value) or isinstance(value, pa.Scalar):
    mask = np.zeros(len(self), dtype=np.bool_)
    mask[key] = True
    data = self._if_else(mask, value, self._data)

else:
    indices = np.arange(len(self))[key]
    if len(indices) != len(value):
        raise ValueError("Length of indexer and values mismatch")
    if len(indices) == 0:
        exit()
    argsort = np.argsort(indices)
    indices = indices[argsort]
    value = value.take(argsort)
    mask = np.zeros(len(self), dtype=np.bool_)
    mask[indices] = True
    data = self._replace_with_mask(self._data, mask, value)

if isinstance(data, pa.Array):
    data = pa.chunked_array([data])
self._data = data
