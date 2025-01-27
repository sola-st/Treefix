# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py
def f(cond1):
    lst = []
    while True:
        if cond1:
            lst.append(1)
        else:
            break
        if lst[-1] > 0:  # lst always has an element here
            break
    exit(lst)

self.assertTransformedEquivalent(f, True)
self.assertTransformedEquivalent(f, False)
