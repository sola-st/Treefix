# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""This is an example of a dense tensor being merged, when outer=inner.

    Sometimes, when promoting, the parent and grandparent ranks are equal.
    Finally, note that merge_dims for Ragged and StructuredTensor would not
    accept this as a valid argument. This should be aligned.
    """
t = array_ops.constant([[[1, 11], [2, 12]], [[3, 13], [4, 14]]])
t2 = structured_tensor._merge_dims_generic(t, 2, 2)
self.assertAllEqual(t2, [[[1, 11], [2, 12]], [[3, 13], [4, 14]]])
