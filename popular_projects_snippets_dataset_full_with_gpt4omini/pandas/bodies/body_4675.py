# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
alpha, beta = 0.3, 0.1
left_tailed = self.prng.beta(alpha, beta, size=100)
assert nanops.nankurt(left_tailed) < 0

alpha, beta = 0.1, 0.3
right_tailed = self.prng.beta(alpha, beta, size=100)
assert nanops.nankurt(right_tailed) > 0
