# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# Cast str fill_value matching other fill_value-taking methods
result = arr1d.take([-1, 1], allow_fill=True, fill_value=str(arr1d[-1]))
expected = arr1d[[-1, 1]]
tm.assert_equal(result, expected)

msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    arr1d.take([-1, 1], allow_fill=True, fill_value="foo")
