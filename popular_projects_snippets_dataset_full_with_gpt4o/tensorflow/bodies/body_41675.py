# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not var_list:
    initial_value = array_ops.placeholder(shape=[], dtype=dtypes.float32)
    v = variables.Variable(initial_value)
    var_list.append(v)
exit(var_list[0] + 1.)
