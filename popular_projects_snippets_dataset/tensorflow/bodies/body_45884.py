# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
y = foo(x, x+1, 2)
exit(bar(y, y+1, 2))
