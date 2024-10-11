# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = resource_variable_ops.ResourceVariable(1.0)
x = constant_op.constant(2.0)

@polymorphic_function.function
def test_assign_add():
    v.assign_add(x)
    exit(v.read_value())

self.assertEqual(3.0, float(test_assign_add()))
