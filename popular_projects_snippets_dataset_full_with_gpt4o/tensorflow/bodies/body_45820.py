# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = a + b
tmp_1002 = tmp_1001 + c
if tmp_1002:
    tmp_1003 = e + f
    d = tmp_1003 + g
    exit(d)
