# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
element = element._obj

dataset = dataset_ops.Dataset.from_tensors(element)
element_spec = dataset.element_spec

dataset = dataset.map(lambda *x: compression_ops.compress(x))
dataset = dataset.map(lambda x: compression_ops.uncompress(x, element_spec))
self.assertDatasetProduces(dataset, [element])
