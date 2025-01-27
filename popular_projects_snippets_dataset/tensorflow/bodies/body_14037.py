# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""This is an example of a dense tensor being merged, when outer=rank.

    Note that outer=rank is equivalent to outer=rank - 1. And yet, from the
    perspective of promote, it is nice to be able to have this functionality
    directly available, because sometimes the rank of the parent equals the
    rank of the child.

    Finally, note that merge_dims for Ragged and StructuredTensor would not
    accept this as a valid argument.

    Note: _merge_dims_generic is private, but these unit tests help to
    discuss the proper API definition.
    """
t = array_ops.constant([[[1, 11], [2, 12]], [[3, 13], [4, 14]]])
t2 = structured_tensor._merge_dims_generic(t, 1, 3)
self.assertAllEqual(t2, [[1, 11, 2, 12], [3, 13, 4, 14]])
