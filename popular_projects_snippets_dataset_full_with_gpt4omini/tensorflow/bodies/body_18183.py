# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(math_ops.reduce_sum(functional_ops.scan_v2(
    lambda _, yi: (x - yi)**2,
    elems=data,
    initializer=constant_op.constant(0.))))
