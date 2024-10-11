# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
test_cases = list()

# pyformat: disable
# pylint: disable=bad-whitespace
# Square cases.
input = np.array([[0, 1, 0],  # pylint: disable=redefined-builtin
                  [1, 0, 1],
                  [1, 1, 1]])
diag = np.array([1, 2, 3])
solution = np.array([[1, 1, 0],
                     [1, 2, 1],
                     [1, 1, 3]])
test_cases.append(({"input": input, "diagonal": diag}, solution))

input = np.array([[[1, 0, 3],
                   [0, 2, 0],
                   [1, 0, 3]],
                  [[4, 0, 4],
                   [0, 5, 0],
                   [2, 0, 6]]])
diag = np.array([[-1,  0, -3],
                 [-4, -5, -6]])
solution = np.array([[[-1, 0,  3],
                      [ 0, 0,  0],
                      [ 1, 0, -3]],
                     [[-4,  0,  4],
                      [ 0, -5,  0],
                      [ 2,  0, -6]]])
test_cases.append(({"input": input, "diagonal": diag}, solution))

# Rectangular cases.
input = np.array([[0, 1, 0],
                  [1, 0, 1]])
diag = np.array([3, 4])
solution = np.array([[3, 1, 0],
                     [1, 4, 1]])
test_cases.append(({"input": input, "diagonal": diag}, solution))

input = np.array([[0, 1],
                  [1, 0],
                  [1, 1]])
diag = np.array([3, 4])
solution = np.array([[3, 1],
                     [1, 4],
                     [1, 1]])
test_cases.append(({"input": input, "diagonal": diag}, solution))

input = np.array([[[1, 0, 3],
                   [0, 2, 0]],
                  [[4, 0, 4],
                   [0, 5, 0]]])
diag = np.array([[-1, -2], [-4, -5]])
solution = np.array([[[-1,  0, 3],
                      [ 0, -2, 0]],
                     [[-4,  0, 4],
                      [ 0, -5, 0]]])
test_cases.append(({"input": input, "diagonal": diag}, solution))
# pylint: enable=bad-whitespace
# pyformat: enable

for test in test_cases:
    self._assertOpOutputMatchesExpected(test[0], test[1], high_level)
