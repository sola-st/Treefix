# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
# GH#42461
data = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=data)

frozen = df.index.names[1:]
assert not com.is_bool_indexer(frozen)

result = df[frozen]
expected = df[[]]
tm.assert_frame_equal(result, expected)
