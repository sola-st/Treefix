# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
obj = index_or_series_obj

res = obj.memory_usage()
res_deep = obj.memory_usage(deep=True)

is_ser = isinstance(obj, Series)
is_object = is_object_dtype(obj) or (
    isinstance(obj, Series) and is_object_dtype(obj.index)
)
is_categorical = is_categorical_dtype(obj.dtype) or (
    isinstance(obj, Series) and is_categorical_dtype(obj.index.dtype)
)
is_object_string = is_dtype_equal(obj, "string[python]") or (
    is_ser and is_dtype_equal(obj.index.dtype, "string[python]")
)

if len(obj) == 0:
    if isinstance(obj, Index):
        expected = 0
    else:
        expected = 108 if IS64 else 64
    assert res_deep == res == expected
elif is_object or is_categorical or is_object_string:
    # only deep will pick them up
    assert res_deep > res
else:
    assert res == res_deep

# sys.getsizeof will call the .memory_usage with
# deep=True, and add on some GC overhead
diff = res_deep - sys.getsizeof(obj)
assert abs(diff) < 100
