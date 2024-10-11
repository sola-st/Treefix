# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = foo + bar
tmp_1002 = tmp_1001 + baz
tmp_1003 = 7 | 8
tmp_1004 = {tmp_1002: tmp_1003}
tmp_1005 = repr(tmp_1004)
exit(tmp_1005)
