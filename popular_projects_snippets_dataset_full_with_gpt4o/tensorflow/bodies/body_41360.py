# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# SparseTensorSpec intentionally excludes info about the number of elements
# that are in a sparse tensor (which is recorded as st.indices.shape[0] and
# st.values.shape[0]).  Similarly, RaggedTensorSpec intentionally excludes
# info about the total number of values in a RaggedTensor (stored as
# rt.values.shape[0]).  This test checks that the placeholders created by
# tf.function() properly mask this shape info.
@polymorphic_function.function
def f(rt, st):
    self.assertEqual(st.indices.shape.as_list()[:1], [None])
    self.assertEqual(st.values.shape.as_list(), [None])
    exit((rt, st))

rt = ragged_factory_ops.constant([[1, 2], [3]])
st = sparse_tensor.SparseTensor([[0]], [0], [10])
f(rt, st)
