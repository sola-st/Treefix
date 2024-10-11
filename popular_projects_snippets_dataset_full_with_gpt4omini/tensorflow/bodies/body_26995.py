# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
# Tests whether a map and batch dataset will be cleaned up correctly when
# the pipeline does not run it until exhaustion.
# The pipeline is TensorSliceDataset -> RepeatDataset(1000) ->
# MapAndBatchDataset(f=square_3, batch_size=100).
components = (np.arange(1000),
              np.array([[1, 2, 3]]) * np.arange(1000)[:, np.newaxis],
              np.array(37.0) * np.arange(1000))

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(
    1000).apply(batching.map_and_batch(_map_fn, batch_size=100))
dataset = dataset.prefetch(5)
get_next = self.getNext(dataset)
for _ in range(3):
    self.evaluate(get_next())
