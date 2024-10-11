# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
sample_op = random_ops.parameterized_truncated_normal(
    shape=(int(1e5),), means=0.8, stddevs=0.05, minvals=-1., maxvals=1.)
new_seed = random_ops.random_uniform([2],
                                     seed=1234,
                                     minval=0,
                                     maxval=(2**31 - 1),
                                     dtype=np.int32)
sample_op_stateless = stateless.stateless_parameterized_truncated_normal(
    shape=(int(1e5),),
    seed=new_seed,
    means=0.8,
    stddevs=0.05,
    minvals=-1.,
    maxvals=1.)

with self.session() as sess:
    samples, samples_stateless = sess.run([sample_op, sample_op_stateless])
    # 0. is more than 16 standard deviations from the mean, and
    # should have a likelihood < 1e-57.
    assert (~np.isnan(samples)).all()
    assert (~np.isnan(samples_stateless)).all()
    self.assertAllGreater(samples, 0.)
    self.assertAllGreater(samples_stateless, 0.)
