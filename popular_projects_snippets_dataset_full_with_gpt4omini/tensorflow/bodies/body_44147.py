# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
if c1:
    if c2:
        exit(1)
for _ in range(n):
    pass
exit(2)
