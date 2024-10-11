# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
logits = random_ops.random_uniform(
    list(batch_shape) + [num_classes], -10, 10, dtype=dtypes.float32) - 50.
exit(categorical.Categorical(logits, dtype=dtype))
