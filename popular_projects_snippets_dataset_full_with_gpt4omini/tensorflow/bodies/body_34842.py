# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    accum_op = q.apply_grad((10.0,))
    extract_t = q.take_grad(2)

    # Applying gradient multiple times to increase size from 0 to 2.
    self.assertEqual(q.num_accumulated().eval(), 0)
    accum_op.run()
    self.assertEqual(q.num_accumulated().eval(), 1)
    accum_op.run()
    self.assertEqual(q.num_accumulated().eval(), 2)

    # Extract will reduce size to 0
    extract_t.op.run()
    self.assertEqual(q.num_accumulated().eval(), 0)

    # Take gradients always sets the size back to 0 if successful.
    accum_op = q.apply_grad((10.0,), local_step=1)
    accum_op.run()
    accum_op.run()
    accum_op.run()
    accum_op.run()
    self.assertEqual(q.num_accumulated().eval(), 4)
    extract_t.op.run()
    self.assertEqual(q.num_accumulated().eval(), 0)
