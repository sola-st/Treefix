# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
path = tmp_path / setup_path
# Invalid.
df = tm.makeDataFrame()

msg = "Can only append to Tables"

with pytest.raises(ValueError, match=msg):
    df.to_hdf(path, "df", append=True, format="f")

with pytest.raises(ValueError, match=msg):
    df.to_hdf(path, "df", append=True, format="fixed")

msg = r"invalid HDFStore format specified \[foo\]"

with pytest.raises(TypeError, match=msg):
    df.to_hdf(path, "df", append=True, format="foo")

with pytest.raises(TypeError, match=msg):
    df.to_hdf(path, "df", append=False, format="foo")

# File path doesn't exist
path = ""
msg = f"File {path} does not exist"

with pytest.raises(FileNotFoundError, match=msg):
    read_hdf(path, "df")
