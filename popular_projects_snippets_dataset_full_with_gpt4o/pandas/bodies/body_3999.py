# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_dict.py
# GH#16769
df = DataFrame.from_dict(data_dict, orient)

result = df.columns
expected = Index(keys, dtype="object", tupleize_cols=False)

tm.assert_index_equal(result, expected)
