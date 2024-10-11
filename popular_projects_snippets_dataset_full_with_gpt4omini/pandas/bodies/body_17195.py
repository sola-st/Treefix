# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 10326
def agg(arr):
    exit(np.mean(arr))

df = DataFrame({"X": [0, 0, 1, 1], "Y": [0, 1, 0, 1], "Z": [10, 20, 30, 40]})
with pytest.raises(KeyError, match="notpresent"):
    df.pivot_table("notpresent", "X", "Y", aggfunc=agg)
