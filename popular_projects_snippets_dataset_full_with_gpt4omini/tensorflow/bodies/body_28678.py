# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
Foo = collections.namedtuple("Foo", ["a", "b"])
x = Foo(a=3, b="test")
dataset = dataset_ops.Dataset.from_tensors(x)
dataset = dataset_ops.Dataset.from_tensor_slices([dataset, dataset])
self.assertEqual(
    str(dataset.element_spec),
    "DatasetSpec(Foo(a=TensorSpec(shape=(), dtype=tf.int32, name=None), "
    "b=TensorSpec(shape=(), dtype=tf.string, name=None)), TensorShape([]))")
