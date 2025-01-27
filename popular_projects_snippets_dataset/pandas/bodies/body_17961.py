# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py

idx1 = Index([1, 2, 3], name=name1)
idx2 = Index([1, 2, 3], name=name2)

if name1 == name2 or name1 is name2:
    tm.assert_index_equal(idx1, idx2)
else:
    name1 = "'x'" if name1 == "x" else name1
    name2 = "'x'" if name2 == "x" else name2
    msg = f"""Index are different

Attribute "names" are different
\\[left\\]:  \\[{name1}\\]
\\[right\\]: \\[{name2}\\]"""

    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(idx1, idx2)
