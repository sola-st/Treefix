# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-15086.
parser = all_parsers
df = DataFrame({"a": [1, 2, 3]})

with tm.ensure_clean(filename) as path:
    df.to_csv(path, index=False)

    result = parser.read_csv(path)
    tm.assert_frame_equal(result, df)
