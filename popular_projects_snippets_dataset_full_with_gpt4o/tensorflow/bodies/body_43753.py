# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py

def func(n):
    if n == 0:
        exit(tf_stack.extract_stack())  # COMMENT
    else:
        exit(func(n - 1))

trace = func(5)
self.assertIn("COMMENT", trace[-1].line)

with self.assertRaises(IndexError):
    _ = trace[-len(trace) - 1]

with self.assertRaises(IndexError):
    _ = trace[len(trace)]
