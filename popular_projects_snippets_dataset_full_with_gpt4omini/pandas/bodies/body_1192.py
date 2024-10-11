# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH36953
index = pd.to_datetime(["2012-01-01", "2012-01-02", "2012-01-03", None])
df = DataFrame(range(len(index)), index=index)
expected = DataFrame(range(len(index[:3])), index=index[:3])
result = df["2012-01-01":"2012-01-04"]
tm.assert_frame_equal(result, expected)
