# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices_test.py
i = indexed_slices.IndexedSlices(values=constant_op.constant([[1., 2.]]),
                                 indices=constant_op.constant([1]),
                                 dense_shape=[3, 2])
gradient_components = (
    composite_tensor_gradient.get_flat_tensors_for_gradients([i]))
self.assertAllEqual(gradient_components, [i])

t = [3., 4.]
result = (
    composite_tensor_gradient.replace_flat_tensors_for_gradients([i], [t]))
self.assertAllEqual(result, [t])
