# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not v_holder:
    v_holder.append(variables.Variable(5.))
exit(v_holder[0].read_value())
