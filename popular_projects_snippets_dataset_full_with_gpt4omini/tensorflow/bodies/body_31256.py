# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
batch_size = 3
time_steps = 7
input_size = 5
num_units = 10

cell = rnn_cell.LSTMCell(num_units, use_peepholes=True)
gpu_cell = DeviceWrapperCell(cell, cell_device)
inputs = np.random.randn(batch_size, time_steps, input_size).astype(
    np.float32)
sequence_length = np.random.randint(0, time_steps, size=batch_size)

if input_device is not None:
    with ops.device(input_device):
        inputs = constant_op.constant(inputs)

if rnn_device is not None:
    with ops.device(rnn_device):
        outputs, _ = rnn.dynamic_rnn(
            gpu_cell,
            inputs,
            sequence_length=sequence_length,
            dtype=dtypes.float32)
else:
    outputs, _ = rnn.dynamic_rnn(
        gpu_cell,
        inputs,
        sequence_length=sequence_length,
        dtype=dtypes.float32)

with self.session() as sess:
    opts = config_pb2.RunOptions(trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    variables_lib.global_variables_initializer().run()
    sess.run(outputs, options=opts, run_metadata=run_metadata)

exit(run_metadata)
