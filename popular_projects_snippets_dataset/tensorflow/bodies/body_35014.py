# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = np.random.uniform(size=list(batch_shape))
p = constant_op.constant(p, dtype=dtypes.float32)
exit(bernoulli.Bernoulli(probs=p, dtype=dtype))
