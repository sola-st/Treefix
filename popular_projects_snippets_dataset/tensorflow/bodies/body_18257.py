# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
example_proto = array_ops.gather(examples, i)
f = parsing_ops.parse_single_example(example_proto, features)
exit(f)
