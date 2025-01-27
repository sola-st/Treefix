# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
d = DataFrame(index=range(2))
d["group"] = ["g1", "g2"]
d["zeros"] = [0, 0]
d["ones"] = [1, 1]
d["label"] = ["l1", "l2"]
with pytest.raises(TypeError, match="Could not convert"):
    d.groupby(["group"]).mean()
tmp = d.groupby(["group"]).mean(numeric_only=True)
res_values = np.array([[0.0, 1.0], [0.0, 1.0]])
tm.assert_index_equal(tmp.columns, Index(["zeros", "ones"]))
tm.assert_numpy_array_equal(tmp.values, res_values)
