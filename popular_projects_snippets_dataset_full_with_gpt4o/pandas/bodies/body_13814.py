# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame([[1, 2], [3, 4]], index=["A", "B"], columns=["X", "Y"])

msg = "resulted in the apply method collapsing to a Series."
with pytest.raises(ValueError, match=msg):
    df.style._apply(lambda x: "x")

msg = "created invalid {} labels"
with pytest.raises(ValueError, match=msg.format("index")):
    df.style._apply(lambda x: [""])

with pytest.raises(ValueError, match=msg.format("index")):
    df.style._apply(lambda x: ["", "", "", ""])

with pytest.raises(ValueError, match=msg.format("index")):
    df.style._apply(lambda x: Series(["a:v;", ""], index=["A", "C"]), axis=0)

with pytest.raises(ValueError, match=msg.format("columns")):
    df.style._apply(lambda x: ["", "", ""], axis=1)

with pytest.raises(ValueError, match=msg.format("columns")):
    df.style._apply(lambda x: Series(["a:v;", ""], index=["X", "Z"]), axis=1)

msg = "returned ndarray with wrong shape"
with pytest.raises(ValueError, match=msg):
    df.style._apply(lambda x: np.array([[""], [""]]), axis=None)
