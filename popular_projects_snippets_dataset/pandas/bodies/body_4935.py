# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

ci = pd.CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=False)
msg = (
    r"Categorical is not ordered for operation min\n"
    r"you can use .as_ordered\(\) to change the Categorical to an ordered one\n"
)
with pytest.raises(TypeError, match=msg):
    ci.min()
msg = (
    r"Categorical is not ordered for operation max\n"
    r"you can use .as_ordered\(\) to change the Categorical to an ordered one\n"
)
with pytest.raises(TypeError, match=msg):
    ci.max()

ci = pd.CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=True)
assert ci.min() == "c"
assert ci.max() == "b"
