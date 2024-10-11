# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#33041 check that falling back to loc doesn't allow non-scalar
#  args to slip in

arr = np.random.randn(6).reshape(3, 2)
df = DataFrame(arr, columns=["A", "A"])

msg = "Invalid call for scalar access"
with pytest.raises(ValueError, match=msg):
    df.at[[1, 2]]
with pytest.raises(ValueError, match=msg):
    df.at[1, ["A"]]
with pytest.raises(ValueError, match=msg):
    df.at[:, "A"]

with pytest.raises(ValueError, match=msg):
    df.at[[1, 2]] = 1
with pytest.raises(ValueError, match=msg):
    df.at[1, ["A"]] = 1
with pytest.raises(ValueError, match=msg):
    df.at[:, "A"] = 1
