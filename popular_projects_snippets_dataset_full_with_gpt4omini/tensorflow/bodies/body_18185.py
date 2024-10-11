# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
del idx
exit(functional_ops.scan_v2(lambda _, i: array_ops.gather(v, i),
                              elems=math_ops.range(v.shape[0]),
                              initializer=0.0))
