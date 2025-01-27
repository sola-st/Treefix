# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# github #13654
fname = os.path.join(dirpath, f"test{k}.sas7bdat")
with pd.read_sas(fname, chunksize=chunksize, encoding="utf-8") as rdr:
    y = 0
    for x in rdr:
        y += x.shape[0]
assert y == rdr.row_count
