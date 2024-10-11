# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
tf_function = def_function.function(f)

exit(control_flow_ops.vectorized_map(
    functools.partial(_jvp, tf_function, primal), tangents))
