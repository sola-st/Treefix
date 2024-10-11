# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(cond_v2.indexed_case(
    z_i, [lambda: branch1(x), lambda: branch2(x), lambda: branch3(x)]))
