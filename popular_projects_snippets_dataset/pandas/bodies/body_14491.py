# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py
df = DataFrame(np.random.rand(4, 5), index=list("abcd"), columns=list("ABCDE"))
with tm.ensure_clean(setup_path) as path:
    msg = r"complib only supports \[.*\] compression."
    with pytest.raises(ValueError, match=msg):
        df.to_hdf(path, "df", complib="foolib")
