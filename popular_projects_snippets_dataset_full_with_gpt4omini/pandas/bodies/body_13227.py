# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# github #14734
fname = os.path.join(dirpath, "test1.sas7bdat")
with pd.read_sas(
    fname, format="sas7bdat", iterator=True, encoding="utf-8"
) as rdr:
    d1 = rdr.read(rdr.row_count + 20)

with pd.read_sas(fname, iterator=True, encoding="utf-8") as rdr:
    d2 = rdr.read(rdr.row_count + 20)
tm.assert_frame_equal(d1, d2)
