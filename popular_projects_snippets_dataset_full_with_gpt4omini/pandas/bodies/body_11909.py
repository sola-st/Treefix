# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# https://github.com/pandas-dev/pandas/issues/37094
parser = all_parsers

N = 1_000_001
df = DataFrame({"a": range(N), "b": np.random.randn(N)})

with tm.ensure_clean() as path:
    df.to_csv(path, index=False)
    result = parser.read_csv(path, index_col=[0])

tm.assert_frame_equal(result, df.set_index("a"))
