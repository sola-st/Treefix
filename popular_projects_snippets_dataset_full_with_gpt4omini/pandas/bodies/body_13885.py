# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-18676, https://bugs.python.org/issue32255
#
# Python's CSV library adds an extraneous '""'
# before the newline when the NaN-value is in
# the first row. Otherwise, only the newline
# character is added. This behavior is inconsistent
# and was patched in https://bugs.python.org/pull_request4672.
df1 = DataFrame([None, 1])
expected1 = """\
""
1.0
"""
with tm.ensure_clean("test.csv") as path:
    df1.to_csv(path, header=None, index=None)
    with open(path) as f:
        assert f.read() == expected1

df2 = DataFrame([1, None])
expected2 = """\
1.0
""
"""
with tm.ensure_clean("test.csv") as path:
    df2.to_csv(path, header=None, index=None)
    with open(path) as f:
        assert f.read() == expected2
