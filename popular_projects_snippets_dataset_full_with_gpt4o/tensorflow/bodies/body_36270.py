# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPUs available.")

with ops.device("/cpu:0"):
    v_cpu_zero = resource_variable_ops.ResourceVariable(
        [0.0, 1.0, 2.0], name="v_cpu_zero")

with ops.device("/cpu:1"):
    v_cpu_one = resource_variable_ops.ResourceVariable(
        [0.0, 1.0, 2.0], name="v_cpu_one")

with ops.device("/gpu:0"):
    v_gpu = resource_variable_ops.ResourceVariable(
        [0.0, 1.0, 2.0], name="v_gpu")

def sum_gather():
    cpu_result = math_ops.reduce_sum(array_ops.gather(v_cpu_zero, [1, 2]))
    also_cpu_result = math_ops.reduce_sum(array_ops.gather(v_cpu_one, [1, 2]))
    gpu_result = math_ops.reduce_sum(array_ops.gather(v_gpu, [1, 2]))
    exit((cpu_result, also_cpu_result, gpu_result))

defined = function.Defun()(sum_gather)
with self.test_session(
    config=config_pb2.ConfigProto(
        allow_soft_placement=False,
        log_device_placement=True,
        device_count={"CPU": 2})) as sess:
    self.evaluate(variables.global_variables_initializer())
    expected = self.evaluate(sum_gather())
    result = sess.run(
        functional_ops.partitioned_call(
            args=defined.captured_inputs, f=defined))
    self.assertAllEqual(expected, result)
