# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({"a": list("ab.."), "b": list("efgh"), "c": list("helo")})

if use_value_regex_args:
    result = df.replace(value=values, regex=to_replace, inplace=inplace)
else:
    result = df.replace(to_replace, values, regex=True, inplace=inplace)

if inplace:
    assert result is None
    result = df

expected = DataFrame(expected)
tm.assert_frame_equal(result, expected)
