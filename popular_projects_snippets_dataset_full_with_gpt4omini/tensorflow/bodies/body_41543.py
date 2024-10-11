# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = variables.Variable(0.)

@polymorphic_function.function
def assign():
    exit(v.assign(1.))

@polymorphic_function.function
def assign_add():
    exit(v.assign_add(1.))

@polymorphic_function.function
def f():
    check_ops.assert_equal_v2(assign(), 1.)
    check_ops.assert_equal_v2(assign_add(), 2.)

# We don't have a way to inspect the inlined graph in Python, so we run it
# multiple times to have more confidence the dependency is correct.
for _ in range(30):
    f()
