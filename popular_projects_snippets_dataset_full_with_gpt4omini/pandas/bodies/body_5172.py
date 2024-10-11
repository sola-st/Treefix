# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#13624
td = Timedelta("1 day")

for left, right in [(td, "a"), ("a", td)]:

    msg = "|".join(
        [
            "unsupported operand type",
            r'can only concatenate str \(not "Timedelta"\) to str',
            "must be str, not Timedelta",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        left + right

    msg = "not supported between instances of"
    with pytest.raises(TypeError, match=msg):
        left > right

    assert not left == right  # pylint: disable=unneeded-not
    assert left != right
