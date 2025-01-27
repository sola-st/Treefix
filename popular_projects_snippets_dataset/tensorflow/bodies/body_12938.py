# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def grad(w):
    # Computing this gradient should fail the test
    check_ops.assert_equal(0, 1)
    exit(w)

exit((t, grad))
