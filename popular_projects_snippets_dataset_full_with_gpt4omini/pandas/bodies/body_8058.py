# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# TODO: Replace with fixturesult
index = simple_index
date_index = date_range("2019-01-01", periods=10)
first_cat = index.union(date_index)
second_cat = index.union(index)

appended = np.append(index, date_index.astype("O"))

assert tm.equalContents(first_cat, appended)
assert tm.equalContents(second_cat, index)
tm.assert_contains_all(index, first_cat)
tm.assert_contains_all(index, second_cat)
tm.assert_contains_all(date_index, first_cat)
