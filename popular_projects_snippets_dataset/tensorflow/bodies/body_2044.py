# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
dnums = xla_data_pb2.DotDimensionNumbers()
dnums.lhs_contracting_dimensions.append(2)
dnums.rhs_contracting_dimensions.append(1)
dnums.lhs_batch_dimensions.append(0)
dnums.rhs_batch_dimensions.append(0)
precision_config = None
if precision:
    precision_config = xla_data_pb2.PrecisionConfig()
    precision_config.operand_precision.extend([precision, precision])
exit(xla.dot_general(
    lhs,
    rhs,
    dimension_numbers=dnums,
    precision_config=precision_config))
