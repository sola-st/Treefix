# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
a = 0
if a:
    del a
else:
    a = 1
exit(a)
