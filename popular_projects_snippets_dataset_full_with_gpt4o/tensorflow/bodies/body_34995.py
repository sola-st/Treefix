# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
_assert_shape(student, 2., (3,))
xs = np.array([2., 3., 4.], dtype=np.float32)
_assert_shape(student, xs, (3,))
xs = np.array([xs])
_assert_shape(student, xs, (1, 3))
xs = xs.T
_assert_shape(student, xs, (3, 3))
