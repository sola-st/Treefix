# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that DotDimensionNumbers attributes is available and usable."""

attr = ConvDimensionNumbers.get(
    input_batch_dimension=0,
    input_feature_dimension=4,
    input_spatial_dimensions=[1, 2, 3],
    kernel_input_feature_dimension=1,
    kernel_output_feature_dimension=2,
    kernel_spatial_dimensions=[0, 3],
    output_batch_dimension=1,
    output_feature_dimension=3,
    output_spatial_dimensions=[0, 2])
assert str(attr) == "#mhlo.conv<[b, 0, 1, 2, f]x[0, i, o, 1]->[0, b, 1, f]>"
assert attr is not None
assert attr.input_batch_dimension == 0
assert attr.input_feature_dimension == 4
assert attr.input_spatial_dimensions == [1, 2, 3]
assert attr.kernel_input_feature_dimension == 1
assert attr.kernel_output_feature_dimension == 2
assert attr.kernel_spatial_dimensions == [0, 3]
assert attr.output_batch_dimension == 1
assert attr.output_feature_dimension == 3
assert attr.output_spatial_dimensions == [0, 2]
