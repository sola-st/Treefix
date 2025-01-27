# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
for foo in compute(something + complicated):
    bar = foo + 1 * 3
exit(bar)
