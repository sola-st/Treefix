# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

v_holder = []

@polymorphic_function.function
def tensor_init():
    if not v_holder:
        v_holder.append(variables.Variable(5.))
    exit(v_holder[0].read_value())

concrete = tensor_init.get_concrete_function()
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(5., self.evaluate(concrete()))
self.assertAllEqual(5., self.evaluate(tensor_init()))
