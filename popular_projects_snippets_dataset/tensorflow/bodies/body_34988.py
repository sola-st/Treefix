# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df = constant_op.constant(4.)
mu = constant_op.constant(3.)
sigma = constant_op.constant(math.sqrt(10.))
n = constant_op.constant(100)

random_seed.set_random_seed(654321)
student = student_t.StudentT(df=df, loc=mu, scale=sigma, name="student_t1")
samples1 = self.evaluate(student.sample(n, seed=123456))

random_seed.set_random_seed(654321)
student2 = student_t.StudentT(df=df, loc=mu, scale=sigma, name="student_t2")
samples2 = self.evaluate(student2.sample(n, seed=123456))

self.assertAllClose(samples1, samples2)
