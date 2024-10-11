# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q1 = data_flow_ops.RandomShuffleQueue(
        1, 0, dtypes_lib.float32, ((),), shared_name="shared_queue")
    q1.enqueue((10.0,)).run()

    # TensorFlow TestCase adds a default graph seed (=87654321). We check if
    # the seed computed from the default graph seed is reproduced.
    seed = 887634792
    q2 = data_flow_ops.RandomShuffleQueue(
        1,
        0,
        dtypes_lib.float32, ((),),
        shared_name="shared_queue",
        seed=seed)

    q1_size_t = q1.size()
    q2_size_t = q2.size()

    self.assertEqual(q1_size_t.eval(), 1)
    self.assertEqual(q2_size_t.eval(), 1)

    self.assertEqual(q2.dequeue().eval(), 10.0)

    self.assertEqual(q1_size_t.eval(), 0)
    self.assertEqual(q2_size_t.eval(), 0)

    q2.enqueue((20.0,)).run()

    self.assertEqual(q1_size_t.eval(), 1)
    self.assertEqual(q2_size_t.eval(), 1)

    self.assertEqual(q1.dequeue().eval(), 20.0)

    self.assertEqual(q1_size_t.eval(), 0)
    self.assertEqual(q2_size_t.eval(), 0)
