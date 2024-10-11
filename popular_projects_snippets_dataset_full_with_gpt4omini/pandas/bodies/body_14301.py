# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py

df = tm.makeTimeDataFrame()
msg = r"[\S]* does not exist"
path = tmp_path / setup_path

# constructor
if mode in ["r", "r+"]:
    with pytest.raises(OSError, match=msg):
        HDFStore(path, mode=mode)

else:
    with HDFStore(path, mode=mode) as store:
        assert store._handle.mode == mode

path = tmp_path / setup_path

# context
if mode in ["r", "r+"]:
    with pytest.raises(OSError, match=msg):
        with HDFStore(path, mode=mode) as store:
            pass
else:
    with HDFStore(path, mode=mode) as store:
        assert store._handle.mode == mode

path = tmp_path / setup_path

# conv write
if mode in ["r", "r+"]:
    with pytest.raises(OSError, match=msg):
        df.to_hdf(path, "df", mode=mode)
    df.to_hdf(path, "df", mode="w")
else:
    df.to_hdf(path, "df", mode=mode)

# conv read
if mode in ["w"]:
    msg = (
        "mode w is not allowed while performing a read. "
        r"Allowed modes are r, r\+ and a."
    )
    with pytest.raises(ValueError, match=msg):
        read_hdf(path, "df", mode=mode)
else:
    result = read_hdf(path, "df", mode=mode)
    tm.assert_frame_equal(result, df)
