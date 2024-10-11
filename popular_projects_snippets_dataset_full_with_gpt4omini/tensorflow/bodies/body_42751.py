# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
if not test_util.is_gpu_available():
    self.skipTest("GPU only")

with ops.device("GPU:0"):
    v = resource_variable_ops.ResourceVariable(1.)

read_handle_on_gpu = resource_variable_ops.read_variable_op(
    v.handle, dtypes.float32)
handle_on_cpu = v.handle.cpu()
read_handle_on_cpu = resource_variable_ops.read_variable_op(
    handle_on_cpu, dtypes.float32)

self.assertAllEqual(read_handle_on_cpu, read_handle_on_gpu)
