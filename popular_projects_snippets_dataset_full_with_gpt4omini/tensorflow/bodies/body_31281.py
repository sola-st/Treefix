# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if not test.is_gpu_available():
    # Can't perform this test w/o a GPU
    exit()

gpu_dev = test.gpu_device_name()
with self.session() as sess:
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        x = array_ops.zeros([1, 1, 3])
        cell = rnn_cell_impl.DeviceWrapper(rnn_cell_impl.GRUCell(3), gpu_dev)
        with ops.device("/cpu:0"):
            outputs, _ = rnn.dynamic_rnn(
                cell=cell, inputs=x, dtype=dtypes.float32)
        run_metadata = config_pb2.RunMetadata()
        opts = config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE)

        sess.run([variables_lib.global_variables_initializer()])
        _ = sess.run(outputs, options=opts, run_metadata=run_metadata)

    cpu_stats, gpu_stats = self._retrieve_cpu_gpu_stats(run_metadata)
    self.assertFalse([s for s in cpu_stats if "gru_cell" in s.node_name])
    self.assertTrue([s for s in gpu_stats if "gru_cell" in s.node_name])
