# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
exit(DataFrame(
    np.dot(obj.values, other.values), index=obj.index, columns=other.columns
))
