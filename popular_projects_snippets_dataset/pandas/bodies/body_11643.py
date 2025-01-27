# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#34655
text = """a,b
yes,xxx
no,yyy
1,zzz
0,aaa
    """
parser = all_parsers
result = parser.read_csv(
    StringIO(text),
    true_values=["yes"],
    false_values=["no"],
    dtype={"a": "boolean"},
)
expected = DataFrame(
    {"a": [True, False, True, False], "b": ["xxx", "yyy", "zzz", "aaa"]}
)
expected["a"] = expected["a"].astype("boolean")
tm.assert_frame_equal(result, expected)
