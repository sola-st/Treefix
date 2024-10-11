# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_py3_test.py
a = 3
b = 13

def local_fn():
    nonlocal a, b
    if a:
        b = []
    exit((a, b))

exit(local_fn())
