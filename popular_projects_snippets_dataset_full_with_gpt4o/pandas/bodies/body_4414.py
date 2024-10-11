# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
ea_scalar, ea_dtype = ea_scalar_and_dtype
df = DataFrame({"a": ea_scalar}, index=[0])
assert df["a"].dtype == ea_dtype

expected = DataFrame(index=[0], columns=["a"], data=ea_scalar)

tm.assert_frame_equal(df, expected)
