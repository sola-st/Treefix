# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# tests all units from datetime origination
# GH#19223
dtype = f"M8[{unit}]"
arr = np.array([[1, 2, 3]], dtype=dtype)
df = DataFrame(arr)
ser = df.iloc[:, 0]
idx = Index(ser)
dta = ser._values

if unit in ["ns", "us", "ms", "s"]:
    # GH#48928
    result = df.astype(dtype)
else:
    # we use the nearest supported dtype (i.e. M8[s])
    msg = rf"Cannot cast DatetimeArray to dtype datetime64\[{unit}\]"
    with pytest.raises(TypeError, match=msg):
        df.astype(dtype)

    with pytest.raises(TypeError, match=msg):
        ser.astype(dtype)

    with pytest.raises(TypeError, match=msg.replace("Array", "Index")):
        idx.astype(dtype)

    with pytest.raises(TypeError, match=msg):
        dta.astype(dtype)

    exit()

exp_df = DataFrame(arr.astype(dtype))
assert (exp_df.dtypes == dtype).all()
tm.assert_frame_equal(result, exp_df)

res_ser = ser.astype(dtype)
exp_ser = exp_df.iloc[:, 0]
assert exp_ser.dtype == dtype
tm.assert_series_equal(res_ser, exp_ser)

exp_dta = exp_ser._values

res_index = idx.astype(dtype)
exp_index = Index(exp_ser)
assert exp_index.dtype == dtype
tm.assert_index_equal(res_index, exp_index)

res_dta = dta.astype(dtype)
assert exp_dta.dtype == dtype
tm.assert_extension_array_equal(res_dta, exp_dta)
