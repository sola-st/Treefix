# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    # Two threads, the first generates (0..69, "a").
    num_a = 70
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_a)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(counter, dtypes.float32)]),
        dense_shape=[1])

    # The second generates (99, "b") 90 times and then stops.
    num_b = 90
    ninety_nine = inp.limit_epochs(
        constant_op.constant(
            99, dtype=dtypes.int64), num_b)
    sparse_ninety_nine = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(ninety_nine, dtypes.float32)]),
        dense_shape=[1])

    # These get joined together and grouped into batches of 5.
    batch_size = 5
    if use_dict:
        batched = inp.batch_join(
            [{
                "c": counter,
                "s": sparse_counter,
                "S": "a"
            }, {
                "c": ninety_nine,
                "s": sparse_ninety_nine,
                "S": "b"
            }],
            batch_size=batch_size)
        batched_fetch = [batched["c"], batched["s"], batched["S"]]
    else:
        batched = inp.batch_join(
            [[counter, sparse_counter, "a"],
             [ninety_nine, sparse_ninety_nine, "b"]],
            batch_size=batch_size)
        batched_fetch = batched

    # Shapes.
    self.assertEqual(3, len(batched_fetch))
    self.assertAllEqual((batch_size,), batched_fetch[0].get_shape().as_list())
    self.assertAllEqual((None, 2),
                        batched_fetch[1].indices.get_shape().as_list())
    self.assertAllEqual((None,),
                        batched_fetch[1].values.get_shape().as_list())
    self.assertAllEqual((2,),
                        batched_fetch[1].dense_shape.get_shape().as_list())
    self.assertAllEqual((batch_size,), batched_fetch[2].get_shape().as_list())

    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # Should see the "a" and "b" threads mixed together.
    all_a = []
    seen_b = 0
    saw_both = 0
    num_batches = (num_a + num_b) // batch_size
    for i in range(num_batches):
        results = self.evaluate(batched_fetch)
        self.assertEqual(3, len(results))
        self.assertEqual(batch_size, len(results[0]))
        self.assertEqual(batch_size, len(results[2]))
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

    # We'd like to see some minimum level of mixing of the results of both
    # threads, but we can't rely on fair thread scheduling, so we just log.
    # self.assertGreater(saw_both, 1)
    tf_logging.info("testTwoThreads%s saw both count: %s",
                    "Dict" if use_dict else "", saw_both)

    # Verify the order of results from "a" were preserved.
    self.assertAllEqual(all_a, np.arange(num_a))
    self.assertEqual(seen_b, num_b)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched_fetch)
    for thread in threads:
        thread.join()
