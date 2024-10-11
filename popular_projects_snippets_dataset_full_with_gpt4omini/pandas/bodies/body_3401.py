# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(data)
expected = df.copy()

if compile_regex:
    to_replace = re.compile(to_replace)

if regex_kwarg:
    regex = to_replace
    to_replace = None
else:
    regex = True

result = df.replace(to_replace, value, inplace=inplace, regex=regex)

if inplace:
    assert result is None
    result = df

if value is np.nan:
    expected_replace_val = np.nan
else:
    expected_replace_val = "..."

expected.loc[expected["a"] == ".", "a"] = expected_replace_val
tm.assert_frame_equal(result, expected)
