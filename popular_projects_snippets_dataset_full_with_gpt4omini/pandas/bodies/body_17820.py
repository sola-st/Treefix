# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_categorical_equal.py
data = [1, 2, 3, 4]
msg = """Categorical are different

Attribute "ordered" are different
\\[left\\]:  False
\\[right\\]: True"""

c1 = Categorical(data, ordered=False)
c2 = Categorical(data, ordered=True)

with pytest.raises(AssertionError, match=msg):
    tm.assert_categorical_equal(c1, c2)
