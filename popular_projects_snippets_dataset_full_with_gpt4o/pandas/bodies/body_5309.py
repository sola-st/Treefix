# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
jan = Period("2000-01", "M")

assert not jan == 1
assert jan != 1

int_or_per = "'(Period|int)'"
msg = f"not supported between instances of {int_or_per} and {int_or_per}"
for left, right in [(jan, 1), (1, jan)]:

    with pytest.raises(TypeError, match=msg):
        left > right
    with pytest.raises(TypeError, match=msg):
        left >= right
    with pytest.raises(TypeError, match=msg):
        left < right
    with pytest.raises(TypeError, match=msg):
        left <= right
