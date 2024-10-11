# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py

def _assert_shape(student, arg, shape):
    self.assertEqual(student.log_prob(arg).get_shape(), shape)
    self.assertEqual(student.prob(arg).get_shape(), shape)

def _check(student):
    _assert_shape(student, 2., (3,))
    xs = np.array([2., 3., 4.], dtype=np.float32)
    _assert_shape(student, xs, (3,))
    xs = np.array([xs])
    _assert_shape(student, xs, (1, 3))
    xs = xs.T
    _assert_shape(student, xs, (3, 3))

_check(student_t.StudentT(df=[2., 3., 4.,], loc=2., scale=1.))
_check(student_t.StudentT(df=7., loc=[2., 3., 4.,], scale=1.))
_check(student_t.StudentT(df=7., loc=3., scale=[2., 3., 4.,]))

def _check2d(student):
    _assert_shape(student, 2., (1, 3))
    xs = np.array([2., 3., 4.], dtype=np.float32)
    _assert_shape(student, xs, (1, 3))
    xs = np.array([xs])
    _assert_shape(student, xs, (1, 3))
    xs = xs.T
    _assert_shape(student, xs, (3, 3))

_check2d(student_t.StudentT(df=[[2., 3., 4.,]], loc=2., scale=1.))
_check2d(student_t.StudentT(df=7., loc=[[2., 3., 4.,]], scale=1.))
_check2d(student_t.StudentT(df=7., loc=3., scale=[[2., 3., 4.,]]))

def _check2d_rows(student):
    _assert_shape(student, 2., (3, 1))
    xs = np.array([2., 3., 4.], dtype=np.float32)  # (3,)
    _assert_shape(student, xs, (3, 3))
    xs = np.array([xs])  # (1,3)
    _assert_shape(student, xs, (3, 3))
    xs = xs.T  # (3,1)
    _assert_shape(student, xs, (3, 1))

_check2d_rows(student_t.StudentT(df=[[2.], [3.], [4.]], loc=2., scale=1.))
_check2d_rows(student_t.StudentT(df=7., loc=[[2.], [3.], [4.]], scale=1.))
_check2d_rows(student_t.StudentT(df=7., loc=3., scale=[[2.], [3.], [4.]]))
