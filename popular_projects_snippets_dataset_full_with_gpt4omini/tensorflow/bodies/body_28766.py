# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
with ops.Graph().as_default():
    iterator = dataset_ops.make_one_shot_iterator(
        dataset_ops.Dataset.from_tensors(37.0))
    next_element = iterator.get_next(name="overridden_name")
    self.assertEqual("overridden_name", next_element.op.name)
