# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session():
    # Do component types and shapes.
    b_a_1 = data_flow_ops.Barrier(
        (dtypes.float32,), shapes=(()), shared_name="b_a")
    b_a_2 = data_flow_ops.Barrier(
        (dtypes.int32,), shapes=(()), shared_name="b_a")
    self.evaluate(b_a_1.barrier_ref)
    with self.assertRaisesOpError("component types"):
        self.evaluate(b_a_2.barrier_ref)

    b_b_1 = data_flow_ops.Barrier(
        (dtypes.float32,), shapes=(()), shared_name="b_b")
    b_b_2 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.int32), shapes=((), ()), shared_name="b_b")
    self.evaluate(b_b_1.barrier_ref)
    with self.assertRaisesOpError("component types"):
        self.evaluate(b_b_2.barrier_ref)

    b_c_1 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32),
        shapes=((2, 2), (8,)),
        shared_name="b_c")
    b_c_2 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shared_name="b_c")
    self.evaluate(b_c_1.barrier_ref)
    with self.assertRaisesOpError("component shapes"):
        self.evaluate(b_c_2.barrier_ref)

    b_d_1 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32), shapes=((), ()), shared_name="b_d")
    b_d_2 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32),
        shapes=((2, 2), (8,)),
        shared_name="b_d")
    self.evaluate(b_d_1.barrier_ref)
    with self.assertRaisesOpError("component shapes"):
        self.evaluate(b_d_2.barrier_ref)

    b_e_1 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32),
        shapes=((2, 2), (8,)),
        shared_name="b_e")
    b_e_2 = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32),
        shapes=((2, 5), (8,)),
        shared_name="b_e")
    self.evaluate(b_e_1.barrier_ref)
    with self.assertRaisesOpError("component shapes"):
        self.evaluate(b_e_2.barrier_ref)
