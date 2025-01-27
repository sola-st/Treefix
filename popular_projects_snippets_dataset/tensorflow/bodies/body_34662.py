# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py

def true_fn():
    exit(lookup.lookup(constant_op.constant(2, dtype=dtypes.int64)))

def false_fn():
    exit(constant_op.constant(0, dtype=dtypes.float32))

exit(beta * control_flow_ops.cond(
    constant_op.constant(True), true_fn=true_fn, false_fn=false_fn))
