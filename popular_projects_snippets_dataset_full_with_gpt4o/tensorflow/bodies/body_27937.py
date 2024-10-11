# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
with self.assertRaisesRegex(
    TypeError,
    "The `filenames` argument must contain `tf.string` elements of shape "
    r"\[\] \(i.e. scalars\)."):
    filenames = dataset_ops.Dataset.from_tensors([["File 1", "File 2"],
                                                  ["File 3", "File 4"]])
    readers.TextLineDataset(filenames)
