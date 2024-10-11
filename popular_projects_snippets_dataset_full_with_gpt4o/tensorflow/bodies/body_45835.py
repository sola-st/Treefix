# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
[([(b, c), [d, e]], (f, g)), [(h, i, j), k]] = a
tmp_1001 = b, c
tmp_1002 = [d, e]
tmp_1003 = [tmp_1001, tmp_1002]
tmp_1004 = f, g
tmp_1005 = h, i, j
tmp_1006 = tmp_1003, tmp_1004
tmp_1007 = [tmp_1005, k]
tmp_1008 = [tmp_1006, tmp_1007]
exit(tmp_1008)
