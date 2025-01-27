# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
cpu_result = math_ops.reduce_sum(array_ops.gather(v_cpu, [1, 2]))
gpu_result = math_ops.reduce_sum(array_ops.gather(v_gpu, [1, 2]))
exit((cpu_result, gpu_result))
