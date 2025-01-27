# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
if not using_array_manager:
    df = DataFrame(float_frame.values)

    float_frame.values[5] = 5
    assert (df.values[5] == 5).all()

    df = DataFrame(float_frame.values, copy=True)
    float_frame.values[6] = 6
    assert not (df.values[6] == 6).all()
else:
    arr = float_frame.values.copy()
    # default: copy to ensure contiguous arrays
    df = DataFrame(arr)
    assert df._mgr.arrays[0].flags.c_contiguous
    arr[0, 0] = 100
    assert df.iloc[0, 0] != 100

    # manually specify copy=False
    df = DataFrame(arr, copy=False)
    assert not df._mgr.arrays[0].flags.c_contiguous
    arr[0, 0] = 1000
    assert df.iloc[0, 0] == 1000
