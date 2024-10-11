# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# https://github.com/pandas-dev/pandas/issues/23553
values = klass(
    [
        Period("2011-01-01", freq="D"),
        Period("2011-01-02", freq="D"),
        pd.NaT,
    ]
)
assert lib.infer_dtype(values, skipna=skipna) == "period"

# periods but mixed freq
values = klass(
    [
        Period("2011-01-01", freq="D"),
        Period("2011-01-02", freq="M"),
        pd.NaT,
    ]
)
# with pd.array this becomes PandasArray which ends up as "unknown-array"
exp = "unknown-array" if klass is pd.array else "mixed"
assert lib.infer_dtype(values, skipna=skipna) == exp
