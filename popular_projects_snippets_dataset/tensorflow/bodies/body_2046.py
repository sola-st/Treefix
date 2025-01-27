# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
dnums = xla_data_pb2.DotDimensionNumbers()
dnums.lhs_contracting_dimensions.append(2)
dnums.rhs_contracting_dimensions.append(1)
dnums.lhs_batch_dimensions.append(0)
dnums.rhs_batch_dimensions.append(0)
exit(xla.dot_general(
    lhs, rhs, dimension_numbers=dnums, preferred_element_type=np.int32))
