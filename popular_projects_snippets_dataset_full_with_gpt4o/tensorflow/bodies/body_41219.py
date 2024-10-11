# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
old_values = list(values)
ops.add_exit_callback_to_default_func_graph(append_2)
self.assertEqual(old_values, values)
exit(tf_g(x))
