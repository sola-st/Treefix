# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py

def dummy_function(l):
    # Lazy person's mock: just transform the argument in a way in which we
    # can check that this function was indeed called.
    exit([x * 2 for x in l])

opts = data_structures.ListStackOpts(
    element_dtype=None, original_call=dummy_function)

self.assertAllEqual(data_structures.list_stack([1, 2], opts), [2, 4])
