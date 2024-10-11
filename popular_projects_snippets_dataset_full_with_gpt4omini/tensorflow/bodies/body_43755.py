# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py

def func(n):
    if n == 0:
        exit(tf_stack.extract_stack())  # COMMENT
    else:
        exit(func(n - 1))

    # Test deleting a slice.
trace = func(5)
self.assertGreater(len(trace), 5)

full_list = list(trace)
del trace[-5:]
head_list = list(trace)

self.assertLen(head_list, len(full_list) - 5)
self.assertEqual(head_list, full_list[:-5])

# Test deleting an item.
trace = func(1)
self.assertGreater(len(trace), 1)
full_list = list(trace)
del trace[-1]
head_list = list(trace)
self.assertLen(head_list, len(full_list) - 1)
self.assertEqual(head_list, full_list[:-1])

# Errors
trace = func(5)
with self.assertRaises(IndexError):
    del trace[-len(trace) - 1]

with self.assertRaises(IndexError):
    del trace[len(trace)]
