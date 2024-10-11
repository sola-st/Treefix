# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
exit(control_flow_ops.while_loop_v2(
    lambda *_: True,
    lambda y, shp: (y + random_ops.random_normal(shp)**2, shp),
    (x, array_ops.shape(x)),
    maximum_iterations=3)[0])
