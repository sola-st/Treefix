# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
df = DataFrame({"col": ['a"a', '"bb"']})
expected = """\
"","col"
"0","a\\"a"
"1","\\"bb\\""
"""

with tm.ensure_clean("test.csv") as path:  # QUOTE_ALL
    df.to_csv(path, quoting=1, doublequote=False, escapechar="\\")
    with open(path) as f:
        assert f.read() == expected

df = DataFrame({"col": ["a,a", ",bb,"]})
expected = """\
,col
0,a\\,a
1,\\,bb\\,
"""

with tm.ensure_clean("test.csv") as path:
    df.to_csv(path, quoting=3, escapechar="\\")  # QUOTE_NONE
    with open(path) as f:
        assert f.read() == expected
