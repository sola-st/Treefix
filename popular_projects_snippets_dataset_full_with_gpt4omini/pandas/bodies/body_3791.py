# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
exit(DataFrame(
    data=np.arange(20).reshape(4, 5),
    columns=list("abcde"),
    index=period_range(start="2000", freq="A", periods=4),
))
