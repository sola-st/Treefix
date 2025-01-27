# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
x, y = a, a + b
(z, y), x = (c, y + b), x + a
exit((z, (y, x)))
