# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
dta_file = datapath("io", "data", "stata", "stata-dta-partially-labeled.dta")
values = ["a", "b", "a", "b", 3.0]
with StataReader(dta_file, chunksize=2) as reader:
    with tm.assert_produces_warning(CategoricalConversionWarning):
        for i, block in enumerate(reader):
            assert list(block.cats) == values[2 * i : 2 * (i + 1)]
            if i < 2:
                idx = pd.Index(["a", "b"])
            else:
                idx = pd.Index([3.0], dtype="float64")
            tm.assert_index_equal(block.cats.cat.categories, idx)
with tm.assert_produces_warning(CategoricalConversionWarning):
    with StataReader(dta_file, chunksize=5) as reader:
        large_chunk = reader.__next__()
direct = read_stata(dta_file)
tm.assert_frame_equal(direct, large_chunk)
