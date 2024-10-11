# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = a + b
tmp_1002 = tmp_1001 + c
with tmp_1002 as d:
    tmp_1003 = 2 * d
    tmp_1004 = tmp_1003 + 1
    print(tmp_1004)
