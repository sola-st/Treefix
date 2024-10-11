# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_equals.py
# GH8437 Verify false negative behavior of equals function for dtype object
arr = [False, np.nan]
s1 = Series(arr)
s2 = s1.copy()
s3 = Series(index=range(2), dtype=object)
s4 = s3.copy()
s5 = s3.copy()
s6 = s3.copy()

s3[:-1] = s4[:-1] = s5[0] = s6[0] = False
assert s1.equals(s1)
assert s1.equals(s2)
assert s1.equals(s3)
assert s1.equals(s4)
assert s1.equals(s5)
assert s5.equals(s6)
