# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
component = constant_op.constant([1.])
side = constant_op.constant(0.)
add = lambda x: x + side
dataset = dataset_ops.Dataset.from_tensor_slices(component).map(add)
value = dataset_ops.make_one_shot_iterator(dataset).get_next()
self.assertIsNone(gradients_impl.gradients(value, component)[0])
self.assertIsNone(gradients_impl.gradients(value, side)[0])
self.assertIsNone(gradients_impl.gradients(value, [component, side])[0])
