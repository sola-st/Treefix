# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
a = DataFrame({"col1": [1, 2]}, index=["c", "a"])

b = DataFrame({"col2": [4, 5]}, index=["b", "a"])

c = DataFrame({"col3": [7, 8]}, index=["a", "b"])

expected = DataFrame(
    {
        "col1": {"a": 2.0, "b": float("nan"), "c": 1.0},
        "col2": {"a": 5.0, "b": 4.0, "c": float("nan")},
        "col3": {"a": 7.0, "b": 8.0, "c": float("nan")},
    }
)
if sort_kw is False:
    expected = expected.reindex(index=["c", "a", "b"])

with tm.assert_produces_warning(None):
    result = a.join([b, c], how="outer", sort=sort_kw)
tm.assert_frame_equal(result, expected)
