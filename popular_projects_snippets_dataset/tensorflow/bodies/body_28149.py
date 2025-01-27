# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
# Tests whether a parallel map dataset will be cleaned up correctly when
# the pipeline does not run it until exhaustion.
# The pipeline is TensorSliceDataset -> MapDataset(square_3) ->
# RepeatDataset(None) -> PrefetchDataset(100).
worker, _ = test_util.create_local_cluster(1, 1)

components = (np.arange(1000),
              np.array([[1, 2, 3]]) * np.arange(1000)[:, np.newaxis],
              np.array(37.0) * np.arange(1000))

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

dataset = (
    dataset_ops.Dataset.from_tensor_slices(components).map(_map_fn)
    .repeat(None).prefetch(10000))

iterator = dataset_ops.make_initializable_iterator(dataset)
init_op = iterator.initializer
get_next = iterator.get_next()

with session.Session(worker[0].target) as sess:
    sess.run(init_op)
    for _ in range(3):
        sess.run(get_next)
