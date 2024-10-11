# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session():
    q_a_1 = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shared_name="q_a")
    q_a_2 = data_flow_ops.FIFOQueue(15, dtypes_lib.float32, shared_name="q_a")
    q_a_1.queue_ref.op.run()
    with self.assertRaisesOpError("capacity"):
        q_a_2.queue_ref.op.run()

    q_b_1 = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shared_name="q_b")
    q_b_2 = data_flow_ops.FIFOQueue(10, dtypes_lib.int32, shared_name="q_b")
    q_b_1.queue_ref.op.run()
    with self.assertRaisesOpError("component types"):
        q_b_2.queue_ref.op.run()

    q_c_1 = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shared_name="q_c")
    q_c_2 = data_flow_ops.FIFOQueue(
        10, dtypes_lib.float32, shapes=[(1, 1, 2, 3)], shared_name="q_c")
    q_c_1.queue_ref.op.run()
    with self.assertRaisesOpError("component shapes"):
        q_c_2.queue_ref.op.run()

    q_d_1 = data_flow_ops.FIFOQueue(
        10, dtypes_lib.float32, shapes=[(1, 1, 2, 3)], shared_name="q_d")
    q_d_2 = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shared_name="q_d")
    q_d_1.queue_ref.op.run()
    with self.assertRaisesOpError("component shapes"):
        q_d_2.queue_ref.op.run()

    q_e_1 = data_flow_ops.FIFOQueue(
        10, dtypes_lib.float32, shapes=[(1, 1, 2, 3)], shared_name="q_e")
    q_e_2 = data_flow_ops.FIFOQueue(
        10, dtypes_lib.float32, shapes=[(1, 1, 2, 4)], shared_name="q_e")
    q_e_1.queue_ref.op.run()
    with self.assertRaisesOpError("component shapes"):
        q_e_2.queue_ref.op.run()

    q_f_1 = data_flow_ops.FIFOQueue(10, dtypes_lib.float32, shared_name="q_f")
    q_f_2 = data_flow_ops.FIFOQueue(
        10, (dtypes_lib.float32, dtypes_lib.int32), shared_name="q_f")
    q_f_1.queue_ref.op.run()
    with self.assertRaisesOpError("component types"):
        q_f_2.queue_ref.op.run()
