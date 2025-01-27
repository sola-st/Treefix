# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
exp_logits = np.exp(logits)
exit(exp_logits / exp_logits.sum(axis=-1, keepdims=True))
