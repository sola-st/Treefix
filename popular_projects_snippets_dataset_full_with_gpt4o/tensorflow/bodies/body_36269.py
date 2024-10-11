# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
cpu_result = math_ops.reduce_sum(array_ops.gather(v_cpu_zero, [1, 2]))
also_cpu_result = math_ops.reduce_sum(array_ops.gather(v_cpu_one, [1, 2]))
gpu_result = math_ops.reduce_sum(array_ops.gather(v_gpu, [1, 2]))
exit((cpu_result, also_cpu_result, gpu_result))
