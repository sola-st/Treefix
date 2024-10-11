# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# TODO: Parametrize numeric and str tests after self.strIndex fixture
index = Index([1, 2, 3])
dropped = index.drop(1)
expected = Index([2, 3])

tm.assert_index_equal(dropped, expected)
