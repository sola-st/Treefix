# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# https://github.com/pandas-dev/pandas/issues/35680
df = DataFrame(["a", "b", "c"])
regex = re.compile("^a$")
result = df.replace({regex: "z"}, regex=True)
expected = DataFrame(["z", "b", "c"])
tm.assert_frame_equal(result, expected)
