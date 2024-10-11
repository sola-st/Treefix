# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
y, shp = control_flow_ops.while_loop_v2(
    lambda *_: True, inner, (y, shp), maximum_iterations=3)
exit(control_flow_ops.while_loop_v2(
    lambda *_: True, inner, (y, shp), maximum_iterations=4))
