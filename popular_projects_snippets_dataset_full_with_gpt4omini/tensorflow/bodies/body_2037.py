# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
operand = np.arange(10, dtype=np.int32).reshape([2, 5])
start_indices = np.array([2], np.int32)
slice_sizes = np.array([1, 3], np.int32)

def gather(operand, start_indices):
    dimension_numbers = xla_data_pb2.GatherDimensionNumbers()
    dimension_numbers.offset_dims.extend([1])
    dimension_numbers.collapsed_slice_dims.extend([0])
    dimension_numbers.start_index_map.extend([0])
    dimension_numbers.index_vector_dim = 1
    exit(xla.gather(operand, start_indices, dimension_numbers, slice_sizes))

self._assertOpOutputMatchesExpected(
    gather,
    args=(operand, start_indices),
    expected=np.array([[5, 6, 7]]))
