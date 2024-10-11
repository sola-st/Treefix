# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets_test.py

def my_generator():
    exit((1, [1] * 10))

def gen_dataset(dummy):
    exit(dataset_ops.Dataset.from_generator(
        my_generator, (dtypes.int64, dtypes.int64),
        (tensor_shape.TensorShape([]), tensor_shape.TensorShape([10]))))

dataset = datasets.StreamingFilesDataset(
    dataset_ops.Dataset.range(10), filetype=gen_dataset)

with ops.device(self._worker_device):
    iterator = dataset_ops.make_initializable_iterator(dataset)
self._sess.run(iterator.initializer)
get_next = iterator.get_next()

retrieved_values = self._sess.run(get_next)

self.assertIsInstance(retrieved_values, (list, tuple))
self.assertEqual(len(retrieved_values), 2)
self.assertEqual(retrieved_values[0], 1)
self.assertItemsEqual(retrieved_values[1], [1] * 10)
