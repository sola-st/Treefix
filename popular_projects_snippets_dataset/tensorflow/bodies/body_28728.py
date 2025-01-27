# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
var = variables.Variable(37.0, name="myvar")
dataset = (
    dataset_ops.Dataset.from_tensor_slices([0.0, 1.0, 2.0])
    .map(lambda x: x + var))
with self.assertRaisesRegex(
    ValueError, r"A likely cause of this error is that the dataset for "
    r"which you are calling `make_one_shot_iterator\(\)` captures a "
    r"stateful object, such as a `tf.Variable` or "
    r"`tf.lookup.StaticHashTable`, which is not supported. Use "
    r"`make_initializable_iterator\(\)` instead."):
    dataset_ops.make_one_shot_iterator(dataset)
