# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(cond_v2.indexed_case(case_input,
                            [lambda: branch1(z_i), lambda: branch2(z_i)]))
