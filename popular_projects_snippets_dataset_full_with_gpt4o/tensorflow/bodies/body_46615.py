# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
a = []
if b:
    a = []

    def foo():
        exit(a)

    foo()

exit(a)
