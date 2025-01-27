# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

msg = (
    r"only list-like objects are allowed to be passed to isin\(\), "
    r"you passed a \[int\]"
)
with pytest.raises(TypeError, match=msg):
    algos.isin(1, 1)
with pytest.raises(TypeError, match=msg):
    algos.isin(1, [1])
with pytest.raises(TypeError, match=msg):
    algos.isin([1], 1)
