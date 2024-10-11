# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
with self.assertRaisesRegex(
    TypeError,
    "The `filenames` argument must contain `tf.string` elements. Got a "
    "dataset of `tf.int32` elements."):
    filenames = dataset_ops.Dataset.from_tensors(0)
    readers.TextLineDataset(filenames)
