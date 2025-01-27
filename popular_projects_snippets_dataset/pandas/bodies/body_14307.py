# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py
# Check if file-defaults can be overridden on a per table basis
df = tm.makeDataFrame()
tmpfile = tmp_path / setup_path
store = HDFStore(tmpfile)
store.append("dfc", df, complevel=9, complib="blosc")
store.append("df", df)
store.close()

with tables.open_file(tmpfile, mode="r") as h5file:
    for node in h5file.walk_nodes(where="/df", classname="Leaf"):
        assert node.filters.complevel == 0
        assert node.filters.complib is None
    for node in h5file.walk_nodes(where="/dfc", classname="Leaf"):
        assert node.filters.complevel == 9
        assert node.filters.complib == "blosc"
