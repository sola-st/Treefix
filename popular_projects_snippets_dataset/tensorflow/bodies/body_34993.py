# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py

def _check(student):
    self.assertEqual(student.mean().get_shape(), (3,))
    self.assertEqual(student.variance().get_shape(), (3,))
    self.assertEqual(student.entropy().get_shape(), (3,))
    self.assertEqual(student.log_prob(2.).get_shape(), (3,))
    self.assertEqual(student.prob(2.).get_shape(), (3,))
    self.assertEqual(student.sample(37).get_shape(), (37, 3,))

_check(student_t.StudentT(df=[2., 3., 4.,], loc=2., scale=1.))
_check(student_t.StudentT(df=7., loc=[2., 3., 4.,], scale=1.))
_check(student_t.StudentT(df=7., loc=3., scale=[2., 3., 4.,]))
