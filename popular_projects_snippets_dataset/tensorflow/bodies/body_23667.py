# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    constant_op.constant([1, 2, 3]))
dataset = dataset.map(lambda x: data_structures._TupleWrapper((x,)))
for index, element in enumerate(dataset):
    self.assertEqual((index + 1,), self.evaluate(element))
