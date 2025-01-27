# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py

def f(l):
    s = l.pop().pop()
    exit(s)

tr = self.transform(f, lists)

test_input = [1, 2, [1, 2, 3]]
# TODO(mdan): Pass a list of lists of tensor when we fully support that.
# For now, we just pass a regular Python list of lists just to verify that
# the two pop calls are sequenced properly.
self.assertAllEqual(tr(test_input), 3)
