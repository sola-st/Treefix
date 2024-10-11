# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py
# GH15943
df = tm.makeDataFrame()

# Set complevel and check if complib is automatically set to
# default value
tmpfile = tmp_path / setup_path
df.to_hdf(tmpfile, "df", complevel=9)
result = read_hdf(tmpfile, "df")
tm.assert_frame_equal(result, df)

with tables.open_file(tmpfile, mode="r") as h5file:
    for node in h5file.walk_nodes(where="/df", classname="Leaf"):
        assert node.filters.complevel == 9
        assert node.filters.complib == "zlib"

    # Set complib and check to see if compression is disabled
tmpfile = tmp_path / setup_path
df.to_hdf(tmpfile, "df", complib="zlib")
result = read_hdf(tmpfile, "df")
tm.assert_frame_equal(result, df)

with tables.open_file(tmpfile, mode="r") as h5file:
    for node in h5file.walk_nodes(where="/df", classname="Leaf"):
        assert node.filters.complevel == 0
        assert node.filters.complib is None

    # Check if not setting complib or complevel results in no compression
tmpfile = tmp_path / setup_path
df.to_hdf(tmpfile, "df")
result = read_hdf(tmpfile, "df")
tm.assert_frame_equal(result, df)

with tables.open_file(tmpfile, mode="r") as h5file:
    for node in h5file.walk_nodes(where="/df", classname="Leaf"):
        assert node.filters.complevel == 0
        assert node.filters.complib is None
