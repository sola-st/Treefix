# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
x = array_ops.unique(x).y
exit(test_ops_for_light_outside_compilation.test_dynamic_tf(
    x, max_size=5))
