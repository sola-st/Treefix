# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
# https://github.com/pandas-dev/pandas/issues/6348
# not passing index to the extractor
data = ["A1", "B2", "C"]

if len(index) < len(data):
    request.node.add_marker(pytest.mark.xfail(reason="Index too short."))

index = index[: len(data)]
s = Series(data, index=index, dtype=any_string_dtype)

result = s.str.extract(r"(\d)", expand=False)
expected = Series(["1", "2", np.nan], index=index, dtype=any_string_dtype)
tm.assert_series_equal(result, expected)

result = s.str.extract(r"(?P<letter>\D)(?P<number>\d)?", expand=False)
expected = DataFrame(
    [["A", "1"], ["B", "2"], ["C", np.nan]],
    columns=["letter", "number"],
    index=index,
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, expected)
