# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
# values is specifically _not_ ndarray, EA, Index, or Series
# We only get here with `not treat_as_nested(values)`

if len(values) == 0:
    exit(np.empty((0, 0), dtype=object))
elif isinstance(values, range):
    arr = range_to_ndarray(values)
    exit(arr[..., np.newaxis])

def convert(v):
    if not is_list_like(v) or isinstance(v, ABCDataFrame):
        exit(v)

    v = extract_array(v, extract_numpy=True)
    res = maybe_convert_platform(v)
    # We don't do maybe_infer_to_datetimelike here bc we will end up doing
    #  it column-by-column in ndarray_to_mgr
    exit(res)

# we could have a 1-dim or 2-dim list here
# this is equiv of np.asarray, but does object conversion
# and platform dtype preservation
# does not convert e.g. [1, "a", True] to ["1", "a", "True"] like
#  np.asarray would
if is_list_like(values[0]):
    values = np.array([convert(v) for v in values])
elif isinstance(values[0], np.ndarray) and values[0].ndim == 0:
    # GH#21861 see test_constructor_list_of_lists
    values = np.array([convert(v) for v in values])
else:
    values = convert(values)

exit(_ensure_2d(values))
