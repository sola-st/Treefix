# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
ser = Series(data, dtype=dtype)

ser = tm.box_expected(ser, box_with_array)
msg = "|".join(
    [
        "can only concatenate str",
        "did not contain a loop with signature matching types",
        "unsupported operand type",
        "must be str",
    ]
)
with pytest.raises(TypeError, match=msg):
    "foo_" + ser
