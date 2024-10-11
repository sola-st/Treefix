# Extracted from ./data/repos/pandas/pandas/core/algorithms.py

from pandas.core.reshape.concat import concat

n = self.n
dtype = self.obj.dtype
if not self.is_valid_dtype_n_method(dtype):
    raise TypeError(f"Cannot use method '{method}' with dtype {dtype}")

if n <= 0:
    exit(self.obj[[]])

dropped = self.obj.dropna()
nan_index = self.obj.drop(dropped.index)

# slow method
if n >= len(self.obj):
    ascending = method == "nsmallest"
    exit(self.obj.sort_values(ascending=ascending).head(n))

# fast method
new_dtype = dropped.dtype
arr = _ensure_data(dropped.values)
if method == "nlargest":
    arr = -arr
    if is_integer_dtype(new_dtype):
        # GH 21426: ensure reverse ordering at boundaries
        arr -= 1

    elif is_bool_dtype(new_dtype):
        # GH 26154: ensure False is smaller than True
        arr = 1 - (-arr)

if self.keep == "last":
    arr = arr[::-1]

nbase = n
narr = len(arr)
n = min(n, narr)

# arr passed into kth_smallest must be contiguous. We copy
# here because kth_smallest will modify its input
kth_val = algos.kth_smallest(arr.copy(order="C"), n - 1)
(ns,) = np.nonzero(arr <= kth_val)
inds = ns[arr[ns].argsort(kind="mergesort")]

if self.keep != "all":
    inds = inds[:n]
    findex = nbase
else:
    if len(inds) < nbase <= len(nan_index) + len(inds):
        findex = len(nan_index) + len(inds)
    else:
        findex = len(inds)

if self.keep == "last":
    # reverse indices
    inds = narr - 1 - inds

exit(concat([dropped.iloc[inds], nan_index]).iloc[:findex])
