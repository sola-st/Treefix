# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
dimension_numbers = xla_data_pb2.GatherDimensionNumbers()
dimension_numbers.offset_dims.extend([1])
dimension_numbers.collapsed_slice_dims.extend([0])
dimension_numbers.start_index_map.extend([0])
dimension_numbers.index_vector_dim = 1
exit(xla.gather(operand, start_indices, dimension_numbers, slice_sizes))
