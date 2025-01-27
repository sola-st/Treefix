# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
# GH 23222
test = DataFrame([1, 2, 2], columns=pd.Index(["A"], name="level_0"))
result = test.groupby([0, 0, 0]).nunique()
expected = DataFrame([2], index=np.array([0]), columns=test.columns)
tm.assert_frame_equal(result, expected)
