# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
dataset = _GetDataSet(batch_size)
iterator = dataset_ops.make_one_shot_iterator(dataset)
features, labels = iterator.get_next()
exit((features, labels))
