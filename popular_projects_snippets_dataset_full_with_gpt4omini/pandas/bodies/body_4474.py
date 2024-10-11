# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame(
    {"A": float_frame["A"], "B": list(float_frame["B"])}, columns=["A", "B"]
)
tm.assert_frame_equal(df, float_frame.loc[:, ["A", "B"]])

msg = "does not match index length"
with pytest.raises(ValueError, match=msg):
    DataFrame({"A": float_frame["A"], "B": list(float_frame["B"])[:-2]})
