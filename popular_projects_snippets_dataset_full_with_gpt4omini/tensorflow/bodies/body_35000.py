# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
mu = [1., 3.3, 4.4]
student = student_t.StudentT(
    df=[0.5, 5., 7.], loc=mu, scale=[3., 2., 1.], allow_nan_stats=False)
with self.assertRaisesOpError("x < y"):
    self.evaluate(student.mean())
