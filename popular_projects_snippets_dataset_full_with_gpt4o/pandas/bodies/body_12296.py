# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame([(1,)], columns=["variable"])
time_stamp = "01 Jan 2000, 00:00:00"
with tm.ensure_clean() as path:
    msg = "time_stamp should be datetime type"
    with pytest.raises(ValueError, match=msg):
        original.to_stata(path, time_stamp=time_stamp, version=version)
    assert not os.path.isfile(path)
