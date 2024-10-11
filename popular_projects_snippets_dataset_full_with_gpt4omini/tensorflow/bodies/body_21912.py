# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    extra_elements = 2
    # Two threads, the first generates (0..69, ["a"] * 1..70).
    num_a = 70 + extra_elements
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_a)

    # The second generates (99, ["b"] * 99) 90 times and then stops.
    num_b = 90 + extra_elements
    ninety_nine = inp.limit_epochs(
        constant_op.constant(
            99, dtype=dtypes.int64), num_b)

    # These get joined together and grouped into batches of 5.
    batch_size = 5
    a = array_ops.tile(
        ["a"],
        math_ops.cast(array_ops.stack([counter + 1]), dtypes.int32))
    b = array_ops.tile(
        ["b"],
        math_ops.cast(array_ops.stack([ninety_nine]), dtypes.int32))
    batched = inp.batch_join(
        [[counter, a], [ninety_nine, b]],
        batch_size=batch_size,
        dynamic_pad=True,
        allow_smaller_final_batch=True)

    # Shapes.
    self.assertEqual(2, len(batched))
    self.assertAllEqual((None,), batched[0].get_shape().as_list())
    self.assertAllEqual((None, None), batched[1].get_shape().as_list())

    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # Should see the "a" and "b" threads mixed together.
    all_a = []
    count_string_a = []
    seen_b = 0
    saw_both = 0
    num_batches = (num_a + num_b) // batch_size
    for i in range(num_batches):
        results = self.evaluate(batched)
        tf_logging.info("Batch %d: %s", i, results[0])
        self.assertEqual(len(results[0]), batch_size)
        self.assertEqual(len(results[1]), batch_size)
        for s in results[1]:
            if s[0] == b"b":
                self.assertAllEqual(s, [b"b"] * 99)
            else:
                count_string_a.append(sum(x == b"a" for x in s))
        which_a = [i for i, s in enumerate(results[1]) if s[0] == b"a"]
        which_b = [i for i, s in enumerate(results[1]) if s[0] == b"b"]
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
    self.assertEqual(len(results[1]), 2 * extra_elements)
    for s in results[1]:
        if s[0] == b"b":
            self.assertAllEqual(s, [b"b"] * 99)
        else:
            count_string_a.append(sum(x == b"a" for x in s))
    which_a = [i for i, s in enumerate(results[1]) if s[0] == b"a"]
    which_b = [i for i, s in enumerate(results[1]) if s[0] == b"b"]
    self.assertEqual(len(which_a) + len(which_b), 2 * extra_elements)
    if which_a and which_b:
        saw_both += 1
    all_a.extend(results[0][i] for i in which_a)
    seen_b += len(which_b)

    # We'd like to see some minimum level of mixing of the results of both
    # threads, but we can't rely on fair thread scheduling, so we just log.
    # self.assertGreater(saw_both, 1)
    tf_logging.info("testTwoThreadsDynamicPadSmallerBatch saw both count: %s",
                    saw_both)

    # Verify the order of results from "a" were preserved.
    self.assertAllEqual(  # tiled "a" with counter + 1
        count_string_a, np.arange(num_a) + 1)
    self.assertAllEqual(all_a, np.arange(num_a))
    self.assertEqual(seen_b, num_b)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
