# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
rng = date_range("1/1/2000", "2/29/2000").as_unit(unit)
df = DataFrame(np.random.randn(3, len(rng)), columns=rng, index=["a", "b", "c"])

result = df.resample("M", axis=1).mean()
expected = df.T.resample("M").mean().T
tm.assert_frame_equal(result, expected)
