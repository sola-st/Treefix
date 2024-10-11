# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
fn = lambda x: [t + 1 for t in x]
with self.assertRaisesRegex(
    TypeError, "iterable_parameters should be a list or tuple of string"):
    dispatch.add_dispatch_support(iterable_parameters="x")(fn)
