# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
sparse_op = getattr(splib, f"sparse_{opname}_float64")
python_op = getattr(operator, opname)

xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
yindex = BlockIndex(TEST_LENGTH, yloc, ylen)

xdindex = xindex.to_int_index()
ydindex = yindex.to_int_index()

x = np.arange(xindex.npoints) * 10.0 + 1
y = np.arange(yindex.npoints) * 100.0 + 1

xfill = 0
yfill = 2

result_block_vals, rb_index, bfill = sparse_op(
    x, xindex, xfill, y, yindex, yfill
)
result_int_vals, ri_index, ifill = sparse_op(
    x, xdindex, xfill, y, ydindex, yfill
)

assert rb_index.to_int_index().equals(ri_index)
tm.assert_numpy_array_equal(result_block_vals, result_int_vals)
assert bfill == ifill

# check versus Series...
xseries = Series(x, xdindex.indices)
xseries = xseries.reindex(np.arange(TEST_LENGTH)).fillna(xfill)

yseries = Series(y, ydindex.indices)
yseries = yseries.reindex(np.arange(TEST_LENGTH)).fillna(yfill)

series_result = python_op(xseries, yseries)
series_result = series_result.reindex(ri_index.indices)

tm.assert_numpy_array_equal(result_block_vals, series_result.values)
tm.assert_numpy_array_equal(result_int_vals, series_result.values)
