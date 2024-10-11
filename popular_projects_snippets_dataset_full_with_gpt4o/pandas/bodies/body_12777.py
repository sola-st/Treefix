# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH 14883
result = json_normalize({"A": {"A": 1, "B": 2}})
expected = DataFrame([[1, 2]], columns=["A.A", "A.B"])
tm.assert_frame_equal(result.reindex_like(expected), expected)

result = json_normalize({"A": {"A": 1, "B": 2}}, sep="_")
expected = DataFrame([[1, 2]], columns=["A_A", "A_B"])
tm.assert_frame_equal(result.reindex_like(expected), expected)

result = json_normalize({"A": {"A": 1, "B": 2}}, sep="\u03c3")
expected = DataFrame([[1, 2]], columns=["A\u03c3A", "A\u03c3B"])
tm.assert_frame_equal(result.reindex_like(expected), expected)

result = json_normalize(
    deep_nested,
    ["states", "cities"],
    meta=["country", ["states", "name"]],
    sep="_",
)
expected = Index(["name", "pop", "country", "states_name"]).sort_values()
assert result.columns.sort_values().equals(expected)
