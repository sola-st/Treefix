# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
dataset = tfds.load('mnist', split='test')
dataset = dataset.map(
    map_func=_PreprocessFn, num_parallel_calls=8).batch(batch_size=batch_size)
dataset = dataset.repeat(count=1)
exit(dataset)
