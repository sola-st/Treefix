# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
tmp_1001 = something + complicated
tmp_1002 = compute(tmp_1001)
for foo in tmp_1002:
    tmp_1003 = 1 * 3
    bar = foo + tmp_1003
exit(bar)
