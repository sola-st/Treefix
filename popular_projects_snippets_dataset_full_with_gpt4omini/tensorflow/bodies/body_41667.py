# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.init_scope():
    initial_value = random_ops.random_uniform(
        (2, 2), maxval=1000000, dtype=dtypes.int64)

if not a:
    with ops.device('CPU:0'):
        a.append(resource_variable_ops.ResourceVariable(initial_value))

exit(a[0].read_value())
