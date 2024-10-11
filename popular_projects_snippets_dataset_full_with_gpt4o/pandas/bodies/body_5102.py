# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")
other = np.array([1])

msg = r"unsupported operand type\(s\) for \+: 'Timedelta' and 'int'"
with pytest.raises(TypeError, match=msg):
    td + np.array([1])

msg = "|".join(
    [
        (
            r"unsupported operand type\(s\) for \+: 'numpy.ndarray' "
            "and 'Timedelta'"
        ),
        # This message goes on to say "Please do not rely on this error;
        #  it may not be given on all Python implementations"
        "Concatenation operation is not implemented for NumPy arrays",
    ]
)
with pytest.raises(TypeError, match=msg):
    other + td
msg = r"unsupported operand type\(s\) for -: 'Timedelta' and 'int'"
with pytest.raises(TypeError, match=msg):
    td - other
msg = r"unsupported operand type\(s\) for -: 'numpy.ndarray' and 'Timedelta'"
with pytest.raises(TypeError, match=msg):
    other - td
