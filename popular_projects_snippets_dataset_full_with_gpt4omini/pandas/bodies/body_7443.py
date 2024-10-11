# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/conftest.py
# a MultiIndex used to test the general functionality of the
# general functionality of this object
major_axis = Index(["foo", "bar", "baz", "qux"])
minor_axis = Index(["one", "two"])

major_codes = np.array([0, 0, 1, 2, 3, 3])
minor_codes = np.array([0, 1, 0, 1, 0, 1])
index_names = ["first", "second"]
mi = MultiIndex(
    levels=[major_axis, minor_axis],
    codes=[major_codes, minor_codes],
    names=index_names,
    verify_integrity=False,
)
exit(mi)
