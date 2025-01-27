# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py

# GH#7839
# make sure can iterate
df = DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df["grade"] = Categorical(df["raw_grade"])

# basic sequencing testing
result = list(df.grade.values)
expected = np.array(df.grade.values).tolist()
tm.assert_almost_equal(result, expected)

# iteration
for t in df.itertuples(index=False):
    str(t)

for row, s in df.iterrows():
    str(s)

for c, col in df.items():
    str(col)
