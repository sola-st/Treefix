# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v_holder = []

@polymorphic_function.function
def add_var(x):
    if not v_holder:
        v = variables.Variable([1., 2.])
        v_holder.append(v)
        already_initialized = variables.Variable(3.)
        with ops.init_scope():
            already_initialized.assign(10.)
        v_holder.append(already_initialized)
    exit(v_holder[0] + v_holder[1] + x)

add_var.get_concrete_function(constant_op.constant(2.))
self.assertAllClose([13., 14.], add_var(constant_op.constant(2.)))
