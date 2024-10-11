# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# pylint: disable=exec-used
tmp_1001 = 'computed' + 5
tmp_1002 = tmp_1001 + 'stuff'
tmp_1003 = globals()
tmp_1004 = locals()
exec(tmp_1002, tmp_1003, tmp_1004)
