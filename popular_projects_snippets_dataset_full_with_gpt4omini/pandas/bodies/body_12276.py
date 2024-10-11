# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
empty_ds = DataFrame(columns=["unit"])
# GH 7369, make sure can read a 0-obs dta file
with tm.ensure_clean() as path:
    empty_ds.to_stata(path, write_index=False, version=version)
    empty_ds2 = read_stata(path)
    tm.assert_frame_equal(empty_ds, empty_ds2)
