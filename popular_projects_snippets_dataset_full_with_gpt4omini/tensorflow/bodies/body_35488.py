# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
shape = [10 * num] if sample_shape is None else sample_shape
generator = gen if gen is not None else (
    stateful_random_ops.Generator.from_seed(seed))
exit(generator.binomial(
    shape=shape, counts=counts, probs=probs, dtype=dtype))
