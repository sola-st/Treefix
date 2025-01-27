# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
with self.cached_session():
    q_a_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shared_name="q_a")
    q_a_2 = data_flow_ops.RandomShuffleQueue(
        15, 5, dtypes_lib.float32, shared_name="q_a")
    q_a_1.queue_ref.op.run()
    with self.assertRaisesOpError("capacity"):
        q_a_2.queue_ref.op.run()

    q_b_1 = data_flow_ops.RandomShuffleQueue(
        10, 0, dtypes_lib.float32, shared_name="q_b")
    q_b_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shared_name="q_b")
    q_b_1.queue_ref.op.run()
    with self.assertRaisesOpError("min_after_dequeue"):
        q_b_2.queue_ref.op.run()

    q_c_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shared_name="q_c")
    q_c_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.int32, shared_name="q_c")
    q_c_1.queue_ref.op.run()
    with self.assertRaisesOpError("component types"):
        q_c_2.queue_ref.op.run()

    q_d_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shared_name="q_d")
    q_d_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shapes=[(1, 1, 2, 3)], shared_name="q_d")
    q_d_1.queue_ref.op.run()
    with self.assertRaisesOpError("component shapes"):
        q_d_2.queue_ref.op.run()

    q_e_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shapes=[(1, 1, 2, 3)], shared_name="q_e")
    q_e_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shared_name="q_e")
    q_e_1.queue_ref.op.run()
    with self.assertRaisesOpError("component shapes"):
        q_e_2.queue_ref.op.run()

    q_f_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shapes=[(1, 1, 2, 3)], shared_name="q_f")
    q_f_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shapes=[(1, 1, 2, 4)], shared_name="q_f")
    q_f_1.queue_ref.op.run()
    with self.assertRaisesOpError("component shapes"):
        q_f_2.queue_ref.op.run()

    q_g_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, shared_name="q_g")
    q_g_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, (dtypes_lib.float32, dtypes_lib.int32), shared_name="q_g")
    q_g_1.queue_ref.op.run()
    with self.assertRaisesOpError("component types"):
        q_g_2.queue_ref.op.run()

    q_h_1 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, seed=12, shared_name="q_h")
    q_h_2 = data_flow_ops.RandomShuffleQueue(
        10, 5, dtypes_lib.float32, seed=21, shared_name="q_h")
    q_h_1.queue_ref.op.run()
    with self.assertRaisesOpError("random seeds"):
        q_h_2.queue_ref.op.run()
