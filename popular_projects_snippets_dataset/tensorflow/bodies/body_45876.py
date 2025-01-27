# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
a = c + d
a.b = c + d
a[b] = c + d
a += c + d
a, b = c
a, b = c, d
a = f(c)
a = f(c + d)
a[b + d] = f.e(c + d)
