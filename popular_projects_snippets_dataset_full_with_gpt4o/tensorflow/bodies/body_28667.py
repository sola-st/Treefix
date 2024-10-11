# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(10)
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError,
                                "make sure that the dataset is created in "
                                "the same graph as the iterator"):
        _ = dataset_ops.make_initializable_iterator(dataset)
