# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    sparse = sparse_tensor.SparseTensor(
        indices=[[0, 1], [0, 2], [1, 0], [1, 3]],
        dense_shape=[2, 4],
        values=[5, 4, 7, 2])
    keep = constant_op.constant([True, False])
    batched = inp.maybe_batch_join([[sparse]],
                                   keep_input=keep,
                                   batch_size=1,
                                   enqueue_many=True)

    with self.cached_session():
        coord = coordinator.Coordinator()
        threads = queue_runner_impl.start_queue_runners(coord=coord)

        batched_np = self.evaluate(batched)

        coord.request_stop()
        for thread in threads:
            thread.join()

    self.assertAllEqual([[0, 1], [0, 2]], batched_np.indices)
    self.assertAllEqual([5, 4], batched_np.values)
    self.assertAllEqual([1, 4], batched_np.dense_shape)
