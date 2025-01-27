# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q1 = data_flow_ops.RandomShuffleQueue(
        1,
        0,
        dtypes_lib.float32, ((),),
        shared_name="shared_queue",
        seed=98765432)
    q1.enqueue((10.0,)).run()

    # If both graph and op seeds are not provided, the default value must be
    # used, and in case a shared queue is already created, the second queue op
    # must accept any previous seed value.
    random_seed.set_random_seed(None)
    q2 = data_flow_ops.RandomShuffleQueue(
        1, 0, dtypes_lib.float32, ((),), shared_name="shared_queue")

    q1_size_t = q1.size()
    q2_size_t = q2.size()

    self.assertEqual(q1_size_t.eval(), 1)
    self.assertEqual(q2_size_t.eval(), 1)
