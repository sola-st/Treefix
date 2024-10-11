# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_attr_equal.py
obj = SimpleNamespace()
obj.na_value = nulls_fixture
tm.assert_attr_equal("na_value", obj, obj)
