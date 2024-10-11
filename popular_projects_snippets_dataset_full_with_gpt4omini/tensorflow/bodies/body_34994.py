# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
self.assertEqual(student.log_prob(arg).get_shape(), shape)
self.assertEqual(student.prob(arg).get_shape(), shape)
