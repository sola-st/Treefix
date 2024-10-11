# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
for shape_dtype in [np.int32, np.int64]:
    shape = np.array([1000], dtype=shape_dtype)
    sample_op = random_ops.parameterized_truncated_normal(
        shape=shape, means=0.0, stddevs=0.1, minvals=-1., maxvals=1.)
    new_seed = random_ops.random_uniform([2],
                                         seed=1234,
                                         minval=0,
                                         maxval=(2**31 - 1),
                                         dtype=np.int32)
    sample_op_stateless = stateless.stateless_parameterized_truncated_normal(
        shape=shape,
        seed=new_seed,
        means=0.0,
        stddevs=0.1,
        minvals=-1.,
        maxvals=1.)

    samples = self.evaluate(sample_op)
    stateless_samples = self.evaluate(sample_op_stateless)
    self.assertAllEqual(samples.shape, shape)
    self.assertAllEqual(stateless_samples.shape, shape)
