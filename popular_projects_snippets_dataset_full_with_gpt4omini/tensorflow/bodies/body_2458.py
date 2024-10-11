# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that GatherDimensionNumbers attributes is available and usable."""

attr = GatherDimensionNumbers.get(
    offset_dims=[1, 2],
    collapsed_slice_dims=[3, 4, 5],
    start_index_map=[6],
    index_vector_dim=7)
assert attr is not None
assert str(attr) == ("#mhlo.gather<offset_dims = [1, 2], "
                     "collapsed_slice_dims = [3, 4, 5], "
                     "start_index_map = [6], "
                     "index_vector_dim = 7>")
assert attr.offset_dims == [1, 2]
assert attr.collapsed_slice_dims == [3, 4, 5]
assert attr.start_index_map == [6]
assert attr.index_vector_dim == 7
