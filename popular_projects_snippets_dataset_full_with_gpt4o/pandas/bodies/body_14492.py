# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py
# GH 7775
mi = MultiIndex.from_arrays([idx, idx])
df = DataFrame(0, index=mi, columns=["a"])
path = tmp_path / setup_path
with pytest.raises(NotImplementedError, match="Saving a MultiIndex"):
    df.to_hdf(path, "df")
