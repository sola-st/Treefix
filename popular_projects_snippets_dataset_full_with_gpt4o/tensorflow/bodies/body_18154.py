# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# We make inputs and sequence_length constant so that multiple session.run
# calls produce the same result.
inputs = constant_op.constant(
    np.random.rand(batch_size, max_steps, state_size), dtype=dtypes.float32)
sequence_length = np.random.randint(0, size=[batch_size], high=max_steps + 1)
sequence_length = constant_op.constant(sequence_length, dtype=dtypes.int32)
exit((inputs, sequence_length))
