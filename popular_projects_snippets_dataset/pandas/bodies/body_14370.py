# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df = DataFrame(columns=["a", "a"], data=[[0, 0]])

path = tmp_path / setup_path
msg = "Columns index has to be unique for fixed format"
with pytest.raises(ValueError, match=msg):
    df.to_hdf(path, "df", format="fixed")

df.to_hdf(path, "df", format="table")
other = read_hdf(path, "df")

tm.assert_frame_equal(df, other)
assert df.equals(other)
assert other.equals(df)
