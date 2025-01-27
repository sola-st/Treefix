# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
# GH#10393
df = df_strings
if "b" in order:

    error_msg = (
        f"Column 'b' has dtype object, "
        f"cannot use method '{nselect_method}' with this dtype"
    )
    with pytest.raises(TypeError, match=error_msg):
        getattr(df, nselect_method)(n, order)
else:
    ascending = nselect_method == "nsmallest"
    result = getattr(df, nselect_method)(n, order)
    expected = df.sort_values(order, ascending=ascending).head(n)
    tm.assert_frame_equal(result, expected)
