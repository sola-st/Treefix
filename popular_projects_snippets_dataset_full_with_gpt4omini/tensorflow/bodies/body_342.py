# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for (text, expected) in [
    ("tf.data.experimental.DatasetStructure", "tf.data.DatasetSpec"),
    ("tf.data.experimental.OptionalStructure", "tf.OptionalSpec"),
    ("tf.data.experimental.RaggedTensorStructure", "tf.RaggedTensorSpec"),
    ("tf.data.experimental.SparseTensorStructure", "tf.SparseTensorSpec"),
    ("tf.data.experimental.Structure", "tf.TypeSpec"),
    ("tf.data.experimental.TensorArrayStructure", "tf.TensorArraySpec"),
    ("tf.data.experimental.TensorStructure", "tf.TensorSpec"),
]:
    _, unused_report, unused_errors, actual = self._upgrade(text)
    self.assertEqual(actual, expected)
