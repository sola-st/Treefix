# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
"""Returns samples from a normal distribution shifted `bias` away from 0."""
value = np.random.randn(*shape) * sigma
exit(value + np.sign(value) * bias)
