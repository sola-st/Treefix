# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_ops.py
interval1 = Interval(*type1)
interval2 = Interval(*type2)
if type1 == type2:
    assert interval1 in interval2
else:
    msg = "^'<=' not supported between instances of"
    with pytest.raises(TypeError, match=msg):
        interval1 in interval2
