# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

v = resource_variable_ops.ResourceVariable(1.0)

@function.Defun()
def AssignAdd():
    v.assign_add(1.0)

op = functional_ops.partitioned_call(
    args=AssignAdd.captured_inputs, f=AssignAdd)
_ = self.evaluate(variables.global_variables_initializer())
_ = self.evaluate(op)
value = self.evaluate(v.read_value())
self.assertEqual(value, 2.0)
