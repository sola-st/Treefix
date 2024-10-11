# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
exit((i + 1, control_flow_ops.cond(i > 2, lambda: a + (x**2),
                                    lambda: a + 3)))
