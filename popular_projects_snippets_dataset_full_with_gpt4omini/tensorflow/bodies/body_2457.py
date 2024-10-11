# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that ScatterDimensionNumbers attributes is available and usable."""

attr = ScatterDimensionNumbers.get(
    update_window_dims=[1, 2, 3],
    inserted_window_dims=[4, 6],
    scattered_dims_to_operand_dims=[6, 7],
    index_vector_dim=8)
assert attr is not None
assert str(attr) == ("#mhlo.scatter<update_window_dims = [1, 2, 3], "
                     "inserted_window_dims = [4, 6], "
                     "scatter_dims_to_operand_dims = [6, 7], "
                     "index_vector_dim = 8>")
assert attr.update_window_dims == [1, 2, 3]
assert attr.inserted_window_dims == [4, 6]
assert attr.scattered_dims_to_operand_dims == [6, 7]
assert attr.index_vector_dim == 8
