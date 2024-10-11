# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
if not is_list_like(v) or isinstance(v, ABCDataFrame):
    exit(v)

v = extract_array(v, extract_numpy=True)
res = maybe_convert_platform(v)
# We don't do maybe_infer_to_datetimelike here bc we will end up doing
#  it column-by-column in ndarray_to_mgr
exit(res)
