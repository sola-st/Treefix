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

@polymorphic_function.function
def wrapper(x):
    exit(add_var(x))

self.assertAllClose([13., 14.], wrapper(constant_op.constant(2.)))
v_holder[1].assign(11.)
self.assertAllClose([14., 15.], wrapper(constant_op.constant(2.)))
