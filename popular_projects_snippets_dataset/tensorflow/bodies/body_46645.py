# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
nonlocal a, b
if a:
    b = []
exit((a, b))
