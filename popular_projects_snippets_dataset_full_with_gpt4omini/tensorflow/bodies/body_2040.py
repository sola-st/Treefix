# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
dnums = xla_data_pb2.ConvolutionDimensionNumbers()
num_spatial_dims = 1
dnums.input_batch_dimension = 0
dnums.input_feature_dimension = 1
dnums.output_batch_dimension = 0
dnums.output_feature_dimension = 1
dnums.kernel_output_feature_dimension = 0
dnums.kernel_input_feature_dimension = 1
dnums.input_spatial_dimensions.extend(range(2, 2 + num_spatial_dims))
dnums.kernel_spatial_dimensions.extend(range(2, 2 + num_spatial_dims))
dnums.output_spatial_dimensions.extend(range(2, 2 + num_spatial_dims))
precision_config = None
if precision:
    precision_config = xla_data_pb2.PrecisionConfig()
    precision_config.operand_precision.extend([precision, precision])
exit(xla.conv(
    lhs,
    rhs,
    window_strides=(1,),
    padding=((2, 1),),
    lhs_dilation=(1,),
    rhs_dilation=(2,),
    dimension_numbers=dnums,
    precision_config=precision_config))
