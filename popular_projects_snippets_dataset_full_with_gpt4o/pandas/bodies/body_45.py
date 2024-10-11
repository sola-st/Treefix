# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# GH 40211
def op(x):
    if np.sum(np.sum(x)) < 10:
        raise ValueError
    exit(x)

df = DataFrame({"A": [1, 2, 3], "B": [400, 500, 600]})
msg = "Transform function failed"

with pytest.raises(ValueError, match=msg):
    df.transform([op])

with pytest.raises(ValueError, match=msg):
    df.transform({"A": op, "B": op})

with pytest.raises(ValueError, match=msg):
    df.transform({"A": [op], "B": [op]})

with pytest.raises(ValueError, match=msg):
    df.transform({"A": [op, "shift"], "B": [op]})
