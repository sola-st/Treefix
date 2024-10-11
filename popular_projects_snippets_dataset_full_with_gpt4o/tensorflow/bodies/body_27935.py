# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
with self.assertRaisesRegex(
    TypeError,
    "The `filenames` argument must contain `tf.string` elements. Got "
    "`tf.int32` elements."):
    readers.TextLineDataset(filenames=0)
