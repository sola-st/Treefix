# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# see gh-21947
df = DataFrame(columns=["a"])
cond = df
assert (cond.dtypes == object).all()

result = df.where(cond)
tm.assert_frame_equal(result, df)
