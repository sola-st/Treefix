# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = foo + bar
with tmp_1001:
    tmp_1002 = x + y
    function(tmp_1002)
tmp_1003 = quux + quozzle
if tmp_1003:
    tmp_1004 = z / w
    function(tmp_1004)
