# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH 6043
# iloc with a list
df = DataFrame(index=[0, 1], columns=[0])
df.iloc[1, 0] = [1, 2, 3]
df.iloc[1, 0] = [1, 2]

result = DataFrame(index=[0, 1], columns=[0])
result.iloc[1, 0] = [1, 2]

tm.assert_frame_equal(result, df)
