# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
a = Series(["a", "b"], index=range(2))
b = Series(range(2), index=range(2))
f = DataFrame({"A": a, "B": b})

a = Series(["a", "b"], index=range(5, 7))
b = Series(range(2), index=range(5, 7))
g = DataFrame({"A": a, "B": b})

exp = DataFrame({"A": list("abab"), "B": [0, 1, 0, 1]}, index=[0, 1, 5, 6])
combined = f.combine_first(g)
tm.assert_frame_equal(combined, exp)
