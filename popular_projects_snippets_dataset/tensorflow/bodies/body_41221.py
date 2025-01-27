# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with self.assertRaisesRegex(RuntimeError, 'when not building a function.'):
    ops.add_exit_callback_to_default_func_graph(lambda: None)
