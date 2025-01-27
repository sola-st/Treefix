# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v = variables.Variable(5.0)
if do_add:
    op = v.assign_add(x)
else:
    op = v.assign_sub(x)
with ops.control_dependencies([op]):
    exit(v.read_value())
