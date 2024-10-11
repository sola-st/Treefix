# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 10813
str_array = [{"names": ["foo", "bar"]}, {"names": ["baz", "qux"]}]
df = DataFrame(str_array)
expected_utf8 = """\
,names
0,"['foo', 'bar']"
1,"['baz', 'qux']"
"""
with tm.ensure_clean("unicode_test.csv") as path:
    df.to_csv(path, encoding="utf-8")
    with open(path) as f:
        assert f.read() == expected_utf8
