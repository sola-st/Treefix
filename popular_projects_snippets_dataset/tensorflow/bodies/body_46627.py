# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
if a:
    a = 0
else:
    a = 1
del a
exit(a)
