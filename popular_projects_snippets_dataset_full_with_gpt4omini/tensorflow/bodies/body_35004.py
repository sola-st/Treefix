# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
# df <= 1 ==> variance not defined
student = student_t.StudentT(df=1., loc=0., scale=1., allow_nan_stats=False)
with self.assertRaisesOpError("x < y"):
    self.evaluate(student.variance())

# df <= 1 ==> variance not defined
student = student_t.StudentT(
    df=0.5, loc=0., scale=1., allow_nan_stats=False)
with self.assertRaisesOpError("x < y"):
    self.evaluate(student.variance())
