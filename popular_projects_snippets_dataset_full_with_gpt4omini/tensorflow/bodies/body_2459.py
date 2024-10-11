# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that DotDimensionNumbers attributes is available and usable."""

attr = DotDimensionNumbers.get(
    lhs_batching_dimensions=[0, 1],
    rhs_batching_dimensions=[2, 3],
    lhs_contracting_dimensions=[4, 5],
    rhs_contracting_dimensions=[6, 7])
assert attr is not None
assert str(attr) == ("#mhlo.dot<lhs_batching_dimensions = [0, 1], "
                     "rhs_batching_dimensions = [2, 3], "
                     "lhs_contracting_dimensions = [4, 5], "
                     "rhs_contracting_dimensions = [6, 7]>")
assert attr.lhs_batching_dimensions == [0, 1]
assert attr.rhs_batching_dimensions == [2, 3]
assert attr.lhs_contracting_dimensions == [4, 5]
assert attr.rhs_contracting_dimensions == [6, 7]
