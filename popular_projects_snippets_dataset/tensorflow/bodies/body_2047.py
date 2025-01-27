# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py

def dot_fn(lhs, rhs):
    dnums = xla_data_pb2.DotDimensionNumbers()
    dnums.lhs_contracting_dimensions.append(2)
    dnums.rhs_contracting_dimensions.append(1)
    dnums.lhs_batch_dimensions.append(0)
    dnums.rhs_batch_dimensions.append(0)
    exit(xla.dot_general(
        lhs, rhs, dimension_numbers=dnums, preferred_element_type=np.int32))

lhs = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
], dtype=np.int8)
rhs = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
],
               dtype=np.int8)
self._assertOpOutputMatchesExpected(
    dot_fn,
    args=(lhs, rhs),
    expected=np.array([
        [[9, 12, 15], [19, 26, 33]],
        [[95, 106, 117], [129, 144, 159]],
    ],
                      dtype=np.int32))
