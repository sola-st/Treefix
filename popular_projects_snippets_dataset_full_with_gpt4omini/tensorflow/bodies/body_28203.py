# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Tests whether a parallel map dataset will be cleaned up correctly when
# the pipeline does not run it until exhaustion.
# The pipeline is TensorSliceDataset -> MapDataset(square_3) ->
# RepeatDataset(1000).
components = (np.arange(1000),
              np.array([[1, 2, 3]]) * np.arange(1000)[:, np.newaxis],
              np.array(37.0) * np.arange(1000))

dataset = self._parallel_map_dataset_factory(components, apply_map, 1000,
                                             100, 100)
# NOTE(mrry): Also test that the prefetching thread is cancelled correctly.
dataset = dataset.prefetch(100)
get_next = self.getNext(dataset)

for _ in range(3):
    self.evaluate(get_next())
