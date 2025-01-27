# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if not test.is_gpu_available():
    exit()  # Test requires access to a GPU

gpu_dev = test.gpu_device_name()
run_metadata = self._execute_rnn_on(input_device=gpu_dev)
cpu_stats, gpu_stats = self._retrieve_cpu_gpu_stats(run_metadata)

def _assert_in(op_str, in_stats, out_stats):
    self.assertTrue(any(op_str in s.node_name for s in in_stats))
    self.assertFalse(any(op_str in s.node_name for s in out_stats))

# Everything happens on GPU
_assert_in("TensorArray", gpu_stats, cpu_stats)
