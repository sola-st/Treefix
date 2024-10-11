# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = c + d
tmp_1002 = a + b
tmp_1003 = -tmp_1001
tmp_1004 = e + f
tmp_1005 = (tmp_1002, tmp_1003, tmp_1004)
exit(tmp_1005)
