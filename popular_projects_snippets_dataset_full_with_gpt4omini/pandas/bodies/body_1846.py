# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

df = test_frame
df["D"] = "foo"
r = df.resample("H")
result = r[["A", "B"]].mean()
expected = pd.concat([r.A.mean(), r.B.mean()], axis=1)
tm.assert_frame_equal(result, expected)

expected = r[["A", "B", "C"]].mean()
with pytest.raises(TypeError, match="Could not convert"):
    r.mean()
result = r.mean(numeric_only=True)
tm.assert_frame_equal(result, expected)
