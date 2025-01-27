# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
tf_value_fn = lambda: constant_op.constant(37.0)
tf_value = tf_value_fn()
iterator = dataset_ops.make_one_shot_iterator(
    dataset_ops.Dataset.from_tensors(tf_value))

self.assertTrue(
    structure.are_compatible(
        dataset_ops.get_structure(iterator), expected_element_structure))
self.assertEqual(expected_output_classes,
                 dataset_ops.get_legacy_output_classes(iterator))
self.assertEqual(expected_output_types,
                 dataset_ops.get_legacy_output_types(iterator))
self.assertEqual(expected_output_shapes,
                 dataset_ops.get_legacy_output_shapes(iterator))
