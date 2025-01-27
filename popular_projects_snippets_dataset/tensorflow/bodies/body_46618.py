# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
a = 0

def child():
    a = 1
    exit(a)

child()
exit(a)
