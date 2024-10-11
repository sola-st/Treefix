# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    extra_elements = 2
    # Two threads, the first generates (0..69, "a").
    num_a = 70 + extra_elements
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_a)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(counter, dtypes.float32)]),
        dense_shape=[1])

    # The second generates (99, "b") 90 times and then stops.
    num_b = 90 + extra_elements
    ninety_nine = inp.limit_epochs(
        constant_op.constant(
            99, dtype=dtypes.int64), num_b)
    sparse_ninety_nine = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(ninety_nine, dtypes.float32)]),
        dense_shape=[1])

    # These get joined together and grouped into batches of 5.
    batch_size = 5
    batched = inp.batch_join(
        [[counter, sparse_counter, "a"],
         [ninety_nine, sparse_ninety_nine, "b"]],
        batch_size=batch_size,
        allow_smaller_final_batch=True)

    # Shapes.
    self.assertEqual(3, len(batched))
    self.assertAllEqual((None,), batched[0].get_shape().as_list())
    self.assertAllEqual((None, 2), batched[1].indices.get_shape().as_list())
    self.assertAllEqual((None,), batched[1].values.get_shape().as_list())
    self.assertAllEqual((2,), batched[1].dense_shape.get_shape().as_list())
    self.assertAllEqual((None,), batched[2].get_shape().as_list())

    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # Should see the "a" and "b" threads mixed together.
    all_a = []
    seen_b = 0
    saw_both = 0
    num_batches = (num_a + num_b) // batch_size
    for i in range(num_batches):
        results = self.evaluate(batched)
        tf_logging.info("Batch %d: %s", i, results[0])
        self.assertEqual(len(results[0]), batch_size)
        self.assertEqual(len(results[2]), batch_size)
        self.assertAllEqual(results[0], results[1].values)
        self.assertAllEqual(
            results[1].indices,
            np.vstack((np.arange(batch_size), np.zeros(batch_size))).T)
        self.assertAllEqual(results[1].dense_shape, [batch_size, 1])
        which_a = [i for i, s in enumerate(results[2]) if s == b"a"]
        which_b = [i for i, s in enumerate(results[2]) if s == b"b"]
        self.assertEqual(len(which_a) + len(which_b), batch_size)
        if which_a and which_b:
            saw_both += 1
        all_a.extend(results[0][i] for i in which_a)
        seen_b += len(which_b)
        self.assertAllEqual([99] * len(which_b),
                            [results[0][i] for i in which_b])

    # Reached the final batch with 2 * extra_elements.
    results = self.evaluate(batched)
    tf_logging.info("Last Batch: %s", results[0])
    self.assertEqual(len(results[0]), 2 * extra_elements)
    self.assertEqual(len(results[2]), 2 * extra_elements)
    self.assertAllEqual(results[0], results[1].values)
    self.assertAllEqual(results[1].indices,
                        np.vstack((np.arange(2 * extra_elements),
                                   np.zeros(2 * extra_elements))).T)
    self.assertAllEqual(results[1].dense_shape, [2 * extra_elements, 1])
    which_a = [i for i, s in enumerate(results[2]) if s == b"a"]
    which_b = [i for i, s in enumerate(results[2]) if s == b"b"]
    self.assertEqual(len(which_a) + len(which_b), 2 * extra_elements)
    if which_a and which_b:
        saw_both += 1
    all_a.extend(results[0][i] for i in which_a)
    seen_b += len(which_b)

    # We'd like to see some minimum level of mixing of the results of both
    # threads, but we can't rely on fair thread scheduling, so we just log.
    # self.assertGreater(saw_both, 1)
    tf_logging.info("testTwoThreadsSmallerBatch saw both count: %s", saw_both)

    # Verify the order of results from "a" were preserved.
    self.assertAllEqual(all_a, np.arange(num_a))
    self.assertEqual(seen_b, num_b)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
