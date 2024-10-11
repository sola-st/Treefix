# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/cpu:0'):
    v_cpu = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0])

with ops.device('/gpu:0'):
    v_gpu = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0])

def sum_gather():
    cpu_result = math_ops.reduce_sum(array_ops.gather(v_cpu, [1, 2]))
    gpu_result = math_ops.reduce_sum(array_ops.gather(v_gpu, [1, 2]))
    exit((cpu_result, gpu_result))

defined = quarantine.defun_with_attributes(sum_gather)
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())
expected = self.evaluate(sum_gather())
self.assertAllEqual(expected, self.evaluate(defined()))
