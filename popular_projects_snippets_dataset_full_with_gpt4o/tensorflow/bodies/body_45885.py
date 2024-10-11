# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = x+1
tmp_1002 = 2
y = foo(x, tmp_1001, tmp_1002)
exit(bar(y, y+1, 2))
