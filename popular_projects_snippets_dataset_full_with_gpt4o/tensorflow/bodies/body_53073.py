# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
exit(control_flow_ops.switch_case(i, [
    lambda: branch0(x), lambda: branch1(x), lambda: branch2(x)]))
