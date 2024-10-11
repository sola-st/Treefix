# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# we accept datetime64[ns], timedelta64[ns], and EADtype
arr = np.array([pd.NaT, pd.NaT], dtype=object)

with pytest.raises(ValueError, match="int64"):
    lib.maybe_convert_objects(
        arr,
        convert_datetime=True,
        convert_timedelta=True,
        dtype_if_all_nat=np.dtype("int64"),
    )
