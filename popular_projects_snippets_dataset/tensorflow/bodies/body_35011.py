# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
with self.assertRaisesOpError(r"Condition x > 0 did not hold"):
    student = student_t.StudentT(
        df=[2, -5.], loc=0., scale=1., validate_args=True, name="S")
    self.evaluate(student.mean())
