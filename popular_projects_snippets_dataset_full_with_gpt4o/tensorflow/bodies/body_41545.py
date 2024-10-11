# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v_plus_one = add_one()
v.assign_add(2.0)
exit(v_plus_one)
