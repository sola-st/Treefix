# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py
# GH14478
df = tm.makeDataFrame()

# Building list of all complibs and complevels tuples
all_complibs = tables.filters.all_complibs
# Remove lzo if its not available on this platform
if not tables.which_lib_version("lzo"):
    all_complibs.remove("lzo")
# Remove bzip2 if its not available on this platform
if not tables.which_lib_version("bzip2"):
    all_complibs.remove("bzip2")

all_levels = range(0, 10)
all_tests = [(lib, lvl) for lib in all_complibs for lvl in all_levels]

for (lib, lvl) in all_tests:
    tmpfile = tmp_path / setup_path
    gname = "foo"

    # Write and read file to see if data is consistent
    df.to_hdf(tmpfile, gname, complib=lib, complevel=lvl)
    result = read_hdf(tmpfile, gname)
    tm.assert_frame_equal(result, df)

    # Open file and check metadata for correct amount of compression
    with tables.open_file(tmpfile, mode="r") as h5table:
        for node in h5table.walk_nodes(where="/" + gname, classname="Leaf"):
            assert node.filters.complevel == lvl
            if lvl == 0:
                assert node.filters.complib is None
            else:
                assert node.filters.complib == lib
