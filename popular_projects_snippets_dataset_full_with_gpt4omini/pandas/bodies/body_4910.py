# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
data = {
    "Dave": "dave@google.com",
    "Steve": "steve@gmail.com",
    "Rob": "rob@gmail.com",
    "Wes": np.nan,
}
data = Series(data, dtype=any_string_dtype)

pat = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"

using_pyarrow = any_string_dtype == "string[pyarrow]"

result = data.str.extract(pat, flags=re.IGNORECASE, expand=True)
assert result.iloc[0].tolist() == ["dave", "google", "com"]

with tm.maybe_produces_warning(PerformanceWarning, using_pyarrow):
    result = data.str.match(pat, flags=re.IGNORECASE)
assert result[0]

with tm.maybe_produces_warning(PerformanceWarning, using_pyarrow):
    result = data.str.fullmatch(pat, flags=re.IGNORECASE)
assert result[0]

result = data.str.findall(pat, flags=re.IGNORECASE)
assert result[0][0] == ("dave", "google", "com")

result = data.str.count(pat, flags=re.IGNORECASE)
assert result[0] == 1

msg = "has match groups"
with tm.assert_produces_warning(
    UserWarning, match=msg, raise_on_extra_warnings=not using_pyarrow
):
    result = data.str.contains(pat, flags=re.IGNORECASE)
assert result[0]
