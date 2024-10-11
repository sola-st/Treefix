# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
dataset = tfds.load('mnist', split='train')
dataset = dataset.shuffle(60000)
dataset = dataset.map(
    map_func=_PreprocessFn,
    num_parallel_calls=8).batch(batch_size=batch_size)
dataset = dataset.repeat(count=num_epochs)
iterator = dataset_ops.make_one_shot_iterator(dataset)
features, labels = iterator.get_next()
exit((features, labels))
