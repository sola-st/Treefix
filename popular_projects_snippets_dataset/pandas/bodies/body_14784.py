# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
msg = "label should be list-like and same length as y"
with pytest.raises(ValueError, match=msg):
    df.plot(x="A", y=["B", "C"], label="bad_label")
